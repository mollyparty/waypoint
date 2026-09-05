"""Regression checks. Version-Timestamp: 2026-09-05 18:00:00 UTC-4."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import memory

spec = importlib.util.spec_from_file_location('catalog_build', memory.ROOT / 'catalog/build.py')
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class MemoryTests(unittest.TestCase):
    def test_healthy_baseline(self):
        self.assertEqual(memory.check()['errors'], [])

    def test_detects_source_drift(self):
        actual = memory.sources()
        actual['README.md'] = 'changed'
        with patch.object(memory, 'sources', return_value=actual):
            self.assertTrue(any('Sources changed' in e for e in memory.check()['errors']))

    def test_detects_dangling_edge(self):
        original = memory.read
        graph = copy.deepcopy(original('graphify-out/graph.json'))
        graph['links'].append({'source': 'missing-node', 'target': 'missing-target'})
        with patch.object(memory, 'read', side_effect=lambda p: graph if p == 'graphify-out/graph.json' else original(p)):
            self.assertTrue(any('Dangling' in e for e in memory.check()['errors']))

    def test_requires_session_note(self):
        with patch.object(memory, 'git', return_value='README.md'):
            with self.assertRaisesRegex(RuntimeError, 'session checkpoint'):
                memory.staged()

    def test_blocks_sensitive_staging(self):
        with patch.object(memory, 'git', return_value='.env.local'):
            with self.assertRaisesRegex(RuntimeError, 'Sensitive'):
                memory.staged()

    def test_blueprint_check_detects_stale_without_writing(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            target = root / 'index.html'
            original = catalog.MARK_START + ' -->\nold\n' + catalog.MARK_END + ' -->'
            target.write_text(original, encoding='utf-8')
            with patch.object(catalog, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'stale'):
                    catalog.inject(target, 'new', check=True)
            self.assertEqual(target.read_text(encoding='utf-8'), original)

    def test_missing_marker_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            target = root / 'index.html'
            target.write_text(catalog.MARK_START, encoding='utf-8')
            with patch.object(catalog, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'exactly one'):
                    catalog.inject(target, 'new', check=True)


if __name__ == '__main__':
    unittest.main()
