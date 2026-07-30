# Waypoint Dual-Platform Strategy: Honoring the Android Requirement

Version-Timestamp: 2026-07-30 18:45:00 UTC-4

Scope: decision-grade analysis of the founder's new requirement that the MVP launch on both iOS and Android, evaluated against the locked concept (DEC-006), the approved 15-feature MVP (`mvp-scope.md`, roughly 25 person-months, 8 to 10 calendar months), and the approved iOS stack (`stack-recommendation.md`, `stack-validation.md`). Every external claim carries a source with URL and access date plus a [verified]/[inferred]/[assumption] tag per `research/00-RESEARCH-PLAYBOOK.md`. All sources accessed 2026-07-30 unless noted.

Executive verdict up front: the Android requirement is honorable, but a truly simultaneous dual launch is the worst way to honor it. The evidence says: (a) iOS carries roughly 85 percent of subscription revenue in this category, so Android adds reach but almost no MVP-stage revenue; (b) every relevant competitor including Strava, AllTrails, and Komoot launched iOS-first, and the category leader Runna covers both platforms from one React Native codebase; (c) the hardest Android-specific risk (background GPS survival against OEM battery killers) is a hardening problem, not a blocker. The recommended path is Option D: rebase the client on React Native before code is written (build has not started, so switching cost is at its lifetime minimum), ship iOS at month 9 to 10, ship Android 4 to 8 weeks later. That honors the requirement for roughly 4 to 6 added person-months instead of the 13 to 15 that dual-native costs, and it protects the 12 to 18 month competitive window that DEC-006 treats as a business requirement.

## 1. The strategic frame: what Android adds and what it costs

### 1.1 Market coverage: what Android actually adds in the target geos

Waypoint's launch sequence is iOS English-first, then Android and more geographies (`concept.md` section 6). The requirement changes the "then". Platform share in the target geos, June 2026:

| Geography | iOS share | Android share | Source |
|---|---|---|---|
| United States | 59.8% | 40.0% | StatCounter, June 2026 [verified] |
| United Kingdom | 51.3% | 48.7% | StatCounter, June 2026 [verified] |
| Europe (whole) | 39.0% | 61.0% | StatCounter, June 2026 [verified] |
| Germany | 39.0% | 60.1% | StatCounter via Axis Intelligence, May 2026 [verified] |
| France | 35.4% | 64.0% | StatCounter via Axis Intelligence, May 2026 [verified] |
| Worldwide | 30.8% | 69.1% | StatCounter, June 2026 [verified] |

Sources: StatCounter mobile OS share pages, https://gs.statcounter.com/os-market-share/mobile/united-states-of-america, https://gs.statcounter.com/os-market-share/mobile/united-kingdom, https://gs.statcounter.com/os-market-share/mobile/europe, https://gs.statcounter.com/os-market-share/mobile/worldwide; country table compiled at https://axis-intelligence.com/iphone-vs-android-market-share/. All accessed 2026-07-30.

No public dataset splits runners specifically by phone OS; the honest proxies point in two directions at once. [inferred]

- Toward iOS: Waypoint's primary segment (committed amateurs, premium subscription buyers, US/UK-weighted at launch) maps onto the demographics where iOS dominates. In the US, 68 percent of 18 to 29 year olds use iPhone, iPhone users skew higher income ($53,251 vs $37,040 average annual income), and 87 percent of US teenagers own an iPhone. [verified] (Adapty, iPhone vs Android behavioral comparison, https://adapty.io/blog/iphone-vs-android-users/, accessed 2026-07-30)
- Toward Android: the moment Waypoint touches continental Europe (a stated expansion geo), Android is the majority platform by 20+ points (Germany, France above). An iOS-only product structurally cannot serve most EU runners. [verified as to the shares; the strategic implication is inferred]

So Android adds: roughly 40 percent of the US market, roughly half of the UK, and the majority of the EU. For a product whose safety-aware routing targets women runners broadly (not only premium-phone owners), Android is also a reach and mission question, not purely a revenue question. [inferred]

### 1.2 The counter-evidence: where the money is

The revenue skew is the most one-sided fact in this document:

| Metric | iOS | Android | Source |
|---|---|---|---|
| Store consumer spend, 2025 | $117B | $49B | Business of Apps App Data Report [verified] |
| Share of app subscription revenue | ~85% | ~15% | Adapty State of In-App Subscriptions 2026 (16,000+ apps, $3B+ processed) [verified] |
| Average monthly app spend per user | $10.40 | $1.40 | Business of Apps via Mirava [verified] |
| Trial-to-paid conversion | 39.0% | 28.5% | Mirava benchmark compilation [verified] |
| Annual-plan install-to-paid conversion | 3.6x Android | baseline | Adapty [verified] |
| Involuntary billing failure rate | 14% | 31% | Mirava benchmark compilation [verified] |
| Share of new subscription app launches, 2026 | ~77% | ~23% | RevenueCat State of Subscription Apps 2026 [verified] |

Sources: https://www.businessofapps.com/data/app-data-report/; https://adapty.io/state-of-in-app-subscriptions-report/; https://adapty.io/blog/mobile-app-monetization-2026/; https://www.mirava.io/blog/ios-vs-android-subscription-revenue-benchmarks; https://www.revenuecat.com/state-of-subscription-apps-2026-business/. All accessed 2026-07-30.

Category color: Health and Fitness is the only category where annual plans dominate (60.6 percent of revenue in 2025) and it has the highest trial-to-paid conversion of any category (35 percent), which rewards exactly the premium iOS-heavy audience Waypoint targets first. [verified] (Adapty, sources above). Android is not irrelevant, but Adapty's own guidance is that Android needs a different monetization strategy, not a copied iOS one, which is additional work, not shared work. [verified]

Implication: at MVP (which launches free per gate decision GD-1, with the paid layer in v1.x), Android contributes users and retention signal but nearly no revenue for the first year. Every person-month spent on Android before the paid layer ships is bought with time from the competitive window. [inferred]

### 1.3 Competitor launch histories: what winners actually did

| App | First mobile launch | Second platform | Gap | Notes |
|---|---|---|---|---|
| Strava | iPhone, March 2011 | Android, June 2011 | ~3 months | Web/GPS-device product since 2009; phone apps added later [verified] |
| AllTrails | iPhone, December 2010 | Android, late 2011 | ~1 year | Android then "quickly overtook the huge head start of our iPhone application" in installs (AllTrails' own PR) [verified] |
| Komoot | iPhone, Germany (2011 era) | Both iOS and Android at 2013 international launch | staged | iPhone-first at home, dual-platform when expanding across Europe (Android-majority geos) [verified] |
| Runna | iOS listed December 11, 2021; official launch March 2022 | Android listed on Google Play in the same era; both platforms served from one React Native codebase | ~simultaneous (cross-platform) | The category leader; acquired by Strava 2025 [verified as to stack and dates; the exact Android ship date is not published, see A16] |
| Joggo | n/a | n/a | n/a | Stack not publicly discoverable; excluded from the framework evidence [verified as to non-discoverability] |

Sources: Strava iPhone launch, https://siliconangle.com/2011/03/29/strava-launches-its-first-iphone-app-uses-data-to-help-runners/; Strava Android launch PR, https://www.prnewswire.com/news-releases/strava-launches-free-android-app-for-cyclists-123738234.html; AllTrails 1M installs PR with the Android timeline quote, https://www.prnewswire.com/news-releases/alltrails-the-leading-digital-network-for-outdoor-enthusiasts-celebrates-one-million-mobile-installs-and-announces-the-retail-launch-of-the-ultimate-outdoor-mapkit-177633061.html; AllTrails iOS first release Dec 17, 2010, https://www.appgoblin.info/apps/405075943; Komoot iPhone-first history, https://techcrunch.com/2014/09/25/komoot-launches-in-the-u-s-so-you-can-enjoy-a-guided-trip-through-the-great-outdoors/ and dual-platform European launch, https://techcrunch.com/2013/08/12/komoot-launches-its-hiking-and-cycling-guide-app-across-european-regions/; Runna iOS first release date, https://appgoblin.info/apps/1594204443; Runna official launch date, https://press.strava.com/articles/strava-to-acquire-runna-a-leading-running-training-app; Runna React Native stack (iOS and Android both React Native, SwiftUI only for the Watch app, RevenueCat for subscriptions), Runna's own engineering job postings, https://builtin.com/job/software-engineer-full-stack-senior/7329479 and https://builtin.com/job/engineering-lead-staff/7273965. All accessed 2026-07-30.

Reading: nobody in this category won by building two native apps simultaneously at seed stage. The two patterns that won are (1) iOS-first, Android within months (Strava) or within a year (AllTrails), and (2) one cross-platform codebase covering both from early on (Runna in React Native, Coopah in Flutter). Komoot went dual-platform precisely when it expanded into Android-majority Europe, which is Waypoint's own stated expansion path. [verified facts, inferred reading]

### 1.4 What dual-platform costs at MVP stage

Three currencies: person-months (direct build and QA), calendar (the competitive window from `positioning.md`), and focus (a solo founder plus two contractors is 2.5 to 3.0 FTE; every Android hour is an hour not spent on route quality, which `mvp-scope.md` names as the real MVP risk). The options in section 2 price each. The unpriced cost that matters most: with two native codebases, every v1.x and v2 feature costs roughly double forever. The paid layer (TS-08 plus P-01, 5.5 pm), the Watch app, street crossings, weather: the approved roadmap's roughly 17 pm of fast-follow work becomes roughly 28 to 30 pm under dual-native. [inferred from the approved v1.x table]

## 2. Four options, costed against the 15-feature MVP

Cost basis. The approved MVP is 22.75 scored pm plus roughly 2 pm release overhead (about 25 pm total). Decomposition for this analysis: roughly 9 to 10 pm of that is platform-independent (GraphHopper engine work, constraint data pipeline, backend, PostGIS moat layers, orchestration API) and roughly 13 to 14 pm is client work (tracking, guidance, maps UI, HealthKit, onboarding, privacy UX, release engineering). [inferred decomposition; assumption A14]

| Option | What ships | Total effort (pm) | Calendar to iOS live | Calendar to Android live | Team implied |
|---|---|---|---|---|---|
| A. Native x2, simultaneous (SwiftUI + Kotlin/Compose) | Two full native apps, one backend | 38 to 40 | 11 to 13 months | same day (coupled) | 4.0 to 4.5 FTE (adds 1.5 to 2 Android FTE) |
| B. Cross-platform, simultaneous (one codebase) | One RN or Flutter app on both, one backend | 29 to 32 | 10 to 12 months | same day (coupled) | 2.5 to 3.0 FTE (skills shift) |
| C. Staged native (iOS as approved, Android team starts month 5) | Two native apps, staggered | 38 to 40 | 8 to 10 months (unchanged) | 12 to 14 months | 2.5 to 3.0 FTE, plus 1.5 to 2 Android FTE from month 5 |
| D. Staged cross-platform (build once, iOS certified first) | One RN or Flutter app, staggered certification | 29 to 31 | 9 to 10 months | 10 to 12 months (4 to 8 week stagger) | 2.5 to 3.0 FTE |

All effort and calendar figures are [inferred] planning estimates built from the approved baseline plus the platform deltas below; they are not quotes. Assumption A15 covers the estimating method.

### Option A: Native times two, simultaneous

Scope math: the roughly 13 to 14 pm iOS client is rebuilt in Kotlin/Jetpack Compose. Some cost is amortized (specs, designs, API contracts, test plans exist), but Android adds back platform-specific work that iOS does not have: Health Connect integration and its Play approval process, foreground-service GPS hardening against OEM battery managers (section 3.8), a hardware QA matrix (Samsung, Pixel, Xiaomi at minimum), and Play data-safety and billing setup. Net Android client delta: roughly 11 to 13 pm plus 1.5 pm Android release overhead. Total roughly 38 to 40 pm. [inferred]

Calendar: "simultaneous" couples the launches, so the slower platform gates both. With hiring lead time for 1.5 to 2 Android FTE (the approved plan's own assumption warns a hiring miss adds 1 to 2 months), realistic joint launch is month 11 to 13. That consumes most of the 12 to 18 month window before anything ships, and the paid layer lands at month 14+ near the window's edge. [inferred]

Focus: the founder (product, iOS, routing) now also coordinates an Android workstream with zero shared client code. This is the highest-coordination option at the exact stage where coordination is the scarcest resource. [inferred]

### Option B: Cross-platform framework, simultaneous

The 2026 framework state, evaluated against Waypoint's specific requirements (background GPS, voice guidance, health integrations, maps):

| Criterion | React Native (0.8x, New Architecture) | Flutter (4.x, Impeller) | Kotlin Multiplatform / Compose MP |
|---|---|---|---|
| 2026 maturity | New Architecture complete as of 0.84; largest ecosystem; ~35 to 43% cross-platform usage share | Stable, strong; ~35 to 46% usage share | KMP stable; Compose Multiplatform stable for iOS mid-2025; adoption tripled from 7% to 23% in 18 months |
| Background GPS for a running app | Proven: transistorsoft react-native-background-geolocation (licensed) is the industry standard; multiple production alternatives | Proven: same vendor's flutter_background_geolocation, plus open alternatives | Native APIs directly (it IS native code); nothing extra needed |
| Health integrations | Actively maintained first-class libraries: @kingstinct/react-native-healthkit (148k weekly downloads) and react-native-health-connect (111k weekly downloads, updated May 2026) | health / flutter_health_connect packages cover both platforms | Direct native APIs both sides |
| Maps | MapLibre React Native integration (community, listed by MapLibre) | maplibre_gl / flutter FFI integration (Feb 2026 newsletter notes full FFI transition) | MapLibre Compose (official) plus MapLibre iOS |
| Turn-by-turn guidance | Ferrostar RN bindings exist but are work-in-progress with no published packages; guidance logic can instead live in shared TypeScript over platform TTS | Ferrostar via platform views; same caveat | Ferrostar ships first-class Swift and Kotlin APIs; best fit |
| Real running/fitness apps shipped | Runna (the category leader, iOS and Android both RN, millions of users, Apple App of the Year finalist 2024) | Coopah (UK run coaching app, Flutter mobile confirmed by its own engineering roles and case study) | No running app discovered on KMP in this pass |
| Hiring pool | Largest (JS/TS) | Smaller (Dart is a documented hiring bottleneck) | Kotlin+Swift both required; two UI layers still written |

Sources: framework state and adoption, https://www.javacodegeeks.com/2026/02/kotlin-multiplatform-vs-flutter-vs-react-native-the-2026-cross-platform-reality.html, https://stora.sh/blog/2026-04-03-react-native-vs-flutter-vs-kotlin-multiplatform-2026, https://theeditorial.news/frameworks/flutter-4-vs-react-native-078-vs-kotlin-multiplatform-app-size-native-parity-and-which-one-ships-mp28g2ri (adoption percentages vary by survey; where sources conflict we treat the direction, not the digits, as the finding); transistorsoft SDK family across RN/Flutter/native, https://github.com/transistorsoft/flutter_background_geolocation; RN health libraries, https://github.com/matinzd/react-native-health-connect/ and https://registry.npmjs.org/@kingstinct/react-native-healthkit; MapLibre ecosystem integrations, https://maplibre.org/projects/native/ and https://maplibre.org/news/2026-03-03-maplibre-newsletter-february-2026/; Ferrostar platform support matrix (RN row marked in progress, no published packages), https://stadiamaps.github.io/ferrostar/; Runna stack, https://builtin.com/job/engineering-lead-staff/7273965; Coopah Flutter stack, https://benestudio.co/building-coopah-smart-running-app-training-algorithm/ and https://djinni.co/jobs/802785-flutter-developer-for-running-start-up/. All accessed 2026-07-30. All [verified] as to the facts; fit judgments are [inferred].

Framework verdict: React Native, and the deciding evidence is Runna. The closest competitor in the exact category, at millions of users and top App Store ratings, ships GPS run tracking, training plans, voice-adjacent workout audio, Garmin/Strava/HealthKit integrations, and RevenueCat subscriptions from one React Native codebase, keeping native Swift only for the Watch app. That is a production existence proof for every hard requirement except our custom turn-by-turn guidance, which is buildable as shared TypeScript logic over platform TTS (running guidance is low-speed and simple, per the approved stack doc). Flutter is a credible runner-up (Coopah proves the category), but the talent pool and the Runna precedent tip it. KMP is rejected for this team size: it still requires writing two UIs, which is most of Option A's cost. [inferred verdict on verified facts]

Option B cost: baseline 25 pm mostly transfers (the client is written once); add native-module work on iOS (Foundation Models bridge, WorkoutKit bridge, roughly 1 to 1.5 pm), Android platform hardening and Health Connect approval (roughly 2 to 2.5 pm), dual-store release engineering and device QA (roughly 1.5 to 2 pm). Total roughly 29 to 32 pm. Calendar 10 to 12 months because simultaneous certification couples the launches and Android QA gates iOS. [inferred]

### Option C: Staged native

iOS proceeds exactly as approved (8 to 10 months, all locked stack choices intact). An Android team (1.5 to 2 contractor FTE) starts month 5 with stable API contracts and shipped iOS designs, rebuilds the client in Kotlin/Compose (11 to 13 pm plus overhead), ships month 12 to 14: within 3 to 4 months of iOS launch. Total program cost roughly 38 to 40 pm, same as Option A, but the spend is sequenced and the iOS launch date carries zero new risk. The permanent tax remains: two client codebases for every future feature, roughly doubling client-side v1.x cost (section 1.4). [inferred]

### Option D: Staged cross-platform

Same single codebase as Option B, but the launches are decoupled: iOS is the certification and beta priority, ships month 9 to 10 (roughly 0 to 1 month later than the approved plan, the slip bought by framework plumbing and the iOS native modules). Android hardening (OEM battery UX, device QA, Play review including the Health Connect access approval that takes roughly 2 weeks of calendar lead time) runs as a tail workstream and ships 4 to 8 weeks after iOS. Total roughly 29 to 31 pm, no added FTE, one codebase forever. [inferred; Health Connect approval lead time verified at https://npmx.dev/package/react-native-health-connect, accessed 2026-07-30]

## 3. Platform-parity technical map

Item by item, for the 10 product requirements the client stack must serve.

| # | Capability | iOS (approved) | Android equivalent | Parity verdict |
|---|---|---|---|---|
| 1 | Health platform | HealthKit (plus iOS 27 workout zones) | Health Connect | Good and improving; see 3.1 |
| 2 | Map rendering | MapKit | Google Maps SDK (free) or MapLibre | MapLibre on BOTH platforms beats MapKit for parity; see 3.2 |
| 3 | On-device AI | Apple Foundation Models | Gemini Nano via AICore / ML Kit GenAI | Worst parity gap in the map; see 3.3 |
| 4 | Voice turn-by-turn | Custom engine over AVSpeechSynthesizer (Ferrostar spike) | Same engine over Android TextToSpeech; Ferrostar has first-class Kotlin support | Parity achievable; see 3.4 |
| 5 | Background GPS run tracking | CoreLocation background mode | Foreground service plus OEM hardening | Hardest Android-specific risk; see 3.8 |
| 6 | Watch | WorkoutKit sync, watch app v1.x | Wear OS | Defer both; see 3.5 |
| 7 | Push | APNs | FCM | Commodity; not in the 15-feature MVP; near-zero impact [inferred] |
| 8 | Subscriptions | StoreKit via RevenueCat | Play Billing via RevenueCat | Full parity; see 3.6 |
| 9 | Privacy zones, consent, AI disclosure | Client UX plus server enforcement | Identical (logic is server/shared) | Neutral [inferred] |
| 10 | Sub-30-second cold-open-to-route | Native SwiftUI | RN New Architecture cold starts 600 to 900 ms vs native 400 to 600 ms | Neutral at the 30 s budget; the route API round trip dominates [verified as to the benchmark figures, https://www.decryptcode.com/blog/react-native-vs-flutter-vs-kmp/, accessed 2026-07-30; inferred conclusion] |

### 3.1 HealthKit vs Health Connect

Health Connect is a framework module built into Android 14 and higher (not uninstallable, zero user setup) and a Play Store app on Android 9 to 13; the Jetpack client library reached 1.1.0 stable; over 500 apps had integrated as of May 2024. For Waypoint's needs: `ExerciseSessionRecord` (workouts), `HeartRateRecord` with series samples and aggregates, `ExerciseRoute` (GPS routes attached to sessions), distance, elevation gain, cadence, and power records all exist. [verified] (Health Connect availability, https://developer.android.com/health-and-fitness/health-connect/availability; get started, https://developer.android.com/health-and-fitness/health-connect/get-started; workout guide including ExerciseRoute and HeartRateRecord, https://developer.android.google.cn/health-and-fitness/health-connect/experiences/workouts; Jetpack 1.1.0 stable, https://developer.android.com/health-and-fitness/health-connect; 500-app figure, https://en.wikipedia.org/wiki/Health_Connect. All accessed 2026-07-30.)

The gaps that matter to Waypoint:

- Training load and readiness: iOS 27 HealthKit now computes workout zones (time in heart rate zones) natively; Health Connect has no equivalent training-load or zones API, so Waypoint computes load from raw heart rate series itself on Android. That is extra shared-logic work, not a blocker, and Waypoint's deterministic training math already assumed doing its own computation. [verified as to the API difference] (Apple WWDC26 workout zones session, https://developer.apple.com/videos/play/wwdc2026/207/, accessed 2026-07-30) [inferred as to the impact]
- Access approval: reading Health Connect data in a Play-distributed app requires a declaration form (up to 7 days) plus a whitelist propagation (5 to 7 further business days). Plan roughly 2 weeks of calendar lead. [verified] (https://npmx.dev/package/react-native-health-connect, accessed 2026-07-30)
- Data-source reality: on iOS the personalization backbone is Apple Watch data in HealthKit. The Android runner's dominant watch brand is Garmin (Garmin ranks second behind the Strava mobile app itself across all recording devices, per Strava's 2025 Year in Sport), and whether Garmin Connect writes the data Waypoint needs into Health Connect was not verified in this pass. This is the single most important Android-parity open question because H6 (health platform as the open personalization pathway) was verified for HealthKit, not for Health Connect. [verified as to the device ranking, https://the5krunner.com/2025/12/04/strava-2025-year-in-sport-report-apple-watch-coros-gen-z/, accessed 2026-07-30; the Garmin-to-Health-Connect question is open, see Open Questions]

### 3.2 Maps: MapKit vs Google Maps SDK vs MapLibre/Mapbox

- Google Maps SDK for Android and iOS: mobile-native map loads are free with unlimited usage even after the March 2025 pricing overhaul. Cost is not the issue; a second map stack, a second styling system, and a Google data-flow to audit are. [verified] (Google Maps Platform pricing list showing Maps SDK "Unlimited" free usage, https://developers.google.com/maps/billing-and-pricing/pricing; Maps SDK for Android usage and billing, https://developers.google.com/maps/documentation/android-sdk/usage-and-billing; both accessed 2026-07-30)
- Mapbox: excellent but metered, and a third-party SDK audit burden, unchanged from the approved stack doc's rejection. [verified in `stack-recommendation.md`]
- MapLibre Native: open source (the pre-license-change Mapbox fork), actively released on both platforms (Android 13.0.0 with Vulkan default; iOS 6.28.0 released July 23, 2026 on Metal), with official or listed integrations for SwiftUI, Jetpack Compose, React Native, and Flutter, and it is the map layer Ferrostar's UI is built on. [verified] (https://maplibre.org/projects/native/; https://maplibre.org/news/2026-03-03-maplibre-newsletter-february-2026/; https://github.com/maplibre/maplibre-native/releases/tag/ios-v6.28.0; Ferrostar map layer, https://www.zleptnig.com/blog/ferrostar-0-50-0-51-maplibre-compose-migration/. All accessed 2026-07-30.)

Verdict: if any dual-platform option is chosen, pick MapLibre on BOTH platforms and drop MapKit. One styling system, one overlay/render behavior to debug, zero usage fees, no third-party data flow (tiles can come from any vector-tile provider, self-hosted later), and direct alignment with Ferrostar. MapKit remains the right answer only in the iOS-only world it was chosen for. This amends a DEC-006-adjacent stack choice and is flagged in section 5. [inferred verdict on verified facts]

### 3.3 On-device AI: Apple Foundation Models vs Gemini Nano/AICore

- Apple: one framework, one ~3B model, every Apple Intelligence device (roughly 30 to 38 percent of active iPhones and rising, per `stack-validation.md`), plus Private Cloud Compute at no API cost. [verified in prior pass]
- Android: Gemini Nano runs in the AICore system service, accessed via ML Kit GenAI APIs or the Prompt API. Device support is a curated flagship list (Pixel 9/10, Galaxy S25/S26, recent OnePlus/Xiaomi/OPPO flagships and peers), fragmented further across nano-v2 vs nano-v3 model versions with different capabilities; Google's own Gemini Intelligence tier requires nano-v3 plus 12 GB RAM. There is no Private Cloud Compute equivalent at zero cost. Coverage among mid-range Android devices (the majority of the EU Android base) is effectively nil in 2026. [verified] (ML Kit GenAI supported device list, https://developers.google.com/ml-kit/genai; Gemini Nano and AICore overview, https://developer.android.com/ai/gemini-nano; nano-v2/v3 device split and Gemini Intelligence requirements, https://9to5google.com/2026/05/15/gemini-intelligence-android-spec-requirements/. All accessed 2026-07-30.)

Verdict: on-device AI parity does not exist in 2026. The privacy-preserving design that works on both platforms is the one the iOS plan already contains as its fallback: deterministic training math plus template-based (non-LLM) explanations everywhere, LLM polish where hardware allows (Foundation Models on capable iPhones, ML Kit GenAI on capable Android flagships), and no health data ever sent to a server-side LLM. This keeps the GDPR Article 9 on-device line absolute on both platforms. A server-side AI fallback for both is technically simple but re-opens the Article 9 surface that `stack-validation.md` calls the load-bearing wall; do not do it for MVP. [inferred design on verified constraints]

### 3.4 Voice guidance

The approved plan already builds guidance in-house (MapKit provides none), so Android adds an output adapter, not a second engine: the on-route tracking, off-route detection, and cue-timing logic is platform-neutral geometry that can live in shared code (TypeScript under Option B/D, Rust via Ferrostar, or Kotlin under Option C), speaking through AVSpeechSynthesizer on iOS and android.speech.tts.TextToSpeech on Android. Ferrostar, already the mandated week-one spike, is production-ready on BOTH platforms with voice guidance via platform-native TTS built in, GraphHopper documented among its compatible routing backends (OSRM-compatible responses), and MapLibre UI on both; its React Native bindings are work-in-progress with no published packages, so under Option B/D Ferrostar would be used via thin native modules or its core logic pattern reimplemented in shared TypeScript. The spike must now answer for two platforms, not one. [verified as to Ferrostar's platform matrix, voice guidance, and GraphHopper compatibility, https://stadiamaps.github.io/ferrostar/ and https://stadiamaps.github.io/ferrostar/route-providers.html and https://www.zleptnig.com/blog/ferrostar-0-50-0-51-maplibre-compose-migration/, accessed 2026-07-30; TextToSpeech is the standard Android platform API, https://developer.android.com/reference/android/speech/tts/TextToSpeech, accessed 2026-07-30; the shared-logic design is inferred]

### 3.5 watchOS vs Wear OS: defer both

The approved plan already defers the Watch app to v1.x (GD-2), with WorkoutKit providing a thin iOS Watch story at near-zero cost. On Android there is no WorkoutKit equivalent to lean on, and the Android runner's watch is more often a Garmin than a Wear OS device (Garmin is the number two recording device across Strava; Wear OS does not appear in the top tier). Verdict: defer both watch platforms; keep the WorkoutKit freebie on iOS; treat Wear OS as a post-traction decision alongside the v1.x Watch app, informed by the same GD-2 screener tripwire. [verified as to the device rankings, the5krunner Year in Sport analysis cited in 3.1; inferred sequencing]

### 3.6 StoreKit vs Play Billing

Full parity through the already-chosen vendor: RevenueCat ships supported SDKs for Swift, Kotlin, Kotlin Multiplatform, Flutter, and React Native, wrapping StoreKit and Google Play Billing behind one entitlement system, with server-side receipt validation on both stores. The approved RevenueCat decision transfers to every option unchanged. One Android nuance: Google Play purchase verification flows can bounce users to a banking app, requiring correct Activity launchMode configuration. [verified] (RevenueCat SDK quickstart platform list, https://www.revenuecat.com/docs/getting-started/quickstart; KMP install doc including the launchMode note, https://www.revenuecat.com/docs/getting-started/installation/kotlin-multiplatform; Flutter install doc, https://www.revenuecat.com/docs/getting-started/installation/flutter. All accessed 2026-07-30.) Android's higher involuntary-churn rate (31 percent of billing failures vs 14 percent on iOS, section 1.2) makes RevenueCat's dunning tooling more valuable, not less. [inferred]

### 3.7 APNs vs FCM

Commodity infrastructure with mature abstractions in every framework option. Push notifications are not among the 15 MVP features, so this is a v1.x concern at most. Impact on every option: negligible. [inferred]

### 3.8 Background location on Android: the hardest platform-specific risk

The shape of the problem, in increasing order of nastiness:

1. Permissions and policy: a running app records while the user is actively exercising, so the compliant pattern is a foreground service of type location with a persistent notification, under while-in-use permission. This avoids the separately-reviewed ACCESS_BACKGROUND_LOCATION Play policy gauntlet. Standard, well-trodden. [verified as to the foreground-service requirement for tracking with the screen off] (community and vendor documentation cited below; Android Doze/App Standby official doc, https://developer.android.com/training/monitoring-device-state/doze-standby, accessed 2026-07-30)
2. Doze and App Standby: official Android power management defers background work, but a correctly-implemented foreground service is largely exempt while the run is active. Manageable with standard engineering. [verified, same source]
3. OEM battery killers: the real risk. Xiaomi (MIUI autostart permission plus battery settings deep link), Samsung One UI (sleeping apps plus separate background limits), Huawei, Oppo, Vivo, and older OnePlus builds ship non-standard power managers that can kill even a compliant foreground service; `PowerManager.isIgnoringBatteryOptimizations()` can return true while the OEM layer still kills the app; there is no unified API; the community catalog dontkillmyapp.com documents per-vendor workarounds and settings deep links. For a running app, a killed tracking service means a lost run, which is a one-star review in this category. [verified] (SolutionBox production post-mortem on background location across real devices, https://www.solutionbox.cz/en/blog/background-location-realne-telefony; practitioner analysis of OEM power managers, https://medium.com/@rana.jashwant07/why-your-android-background-location-still-gets-killed-and-how-to-fight-oem-power-managers-fe2289ded489; dontkillmyapp vendor catalog, https://dontkillmyapp.com/general and https://dontkillmyapp.com/google. All accessed 2026-07-30.)

Mitigation posture (applies to every option that ships Android): use a battle-tested tracking layer rather than hand-rolled service code (the transistorsoft background-geolocation SDK family is the de facto standard across native, RN, and Flutter, with native SQLite persistence so fixes survive process death); detect manufacturer at runtime and guide users to the right OEM setting during onboarding without blocking on it; persist and recover run state across service death; and test on physical Samsung and Xiaomi hardware, because emulators do not simulate OEM battery layers. Budget roughly 1 to 1.5 pm for this hardening in every Android-shipping option; it is included in the section 2 estimates. [verified as to the SDK family and techniques, https://github.com/transistorsoft/flutter_background_geolocation and the SolutionBox source above; inferred budget]

One honest note the other direction: this foreground-service pattern is what every Android running app (Strava, Runna, adidas Running) lives with successfully. It is a tax, not a wall. [inferred]

## 4. Impact statement per option

Baseline for comparison: approved plan is roughly 25 pm, iOS live month 8 to 10, paid layer month 10 to 12, consuming at most 10 months of the 12 to 18 month Strava window before launch.

| Option | Total effort | iOS live | Android live | Paid layer lands | Burn vs approved | Window verdict |
|---|---|---|---|---|---|---|
| Approved (iOS only) | ~25 pm | month 8 to 10 | not shipped | month 10 to 12 | baseline | Fits with margin |
| A. Native x2 simultaneous | 38 to 40 pm | month 11 to 13 | month 11 to 13 | month 14 to 16 | +55 to 60% effort; +1.5 to 2 FTE for the whole program | ENDANGERS THE WINDOW. Both launches gated by the slower platform; paid layer lands at or past the window's optimistic edge. Blunt version: this option risks shipping second to Strava on Waypoint's own differentiator. |
| B. Cross-platform simultaneous | 29 to 32 pm | month 10 to 12 | month 10 to 12 | month 12 to 14 | +20 to 28% effort; same headcount | Strains the window. Cheaper than A but still couples iOS to Android certification and hardware QA; one Android surprise (an OEM tracking bug in beta) delays iOS for no iOS reason. |
| C. Staged native | 38 to 40 pm | month 8 to 10 (unchanged) | month 12 to 14 | month 10 to 12 (unchanged) | +55 to 60% effort, sequenced; +1.5 to 2 FTE from month 5 | Window safe for iOS. But it is the most expensive path in total, and it locks in the permanent two-codebase tax: the ~17 pm v1.x roadmap becomes ~28 to 30 pm, slowing every post-launch move inside the window's back half. |
| D. Staged cross-platform | 29 to 31 pm | month 9 to 10 | month 10 to 12 | month 11 to 13 | +16 to 24% effort; same headcount | Window safe with a small toll (roughly 0 to 1 month on iOS). Android ships 4 to 8 weeks behind iOS; one codebase keeps the v1.x roadmap at its approved cost. |

All rows [inferred] from the section 2 estimates; the window arithmetic follows `mvp-scope.md` section 7 and `positioning.md`'s 12 to 18 month assumption (A17 carries the window assumption forward).

## 5. Recommendation

**Recommended: Option D. React Native (with Expo tooling), one codebase, MapLibre maps on both platforms, iOS ships first at month 9 to 10, Android certified 4 to 8 weeks later.**

Ranked against the founder's two stated goals:

1. Market coverage: Android ships within the MVP era (weeks after iOS, not quarters), covering the 40 percent US / 49 percent UK Android base and unlocking the EU expansion geo where Android is the majority platform. Coverage goal honored in full, with a stagger measured in weeks. [inferred from sections 1.1 and 2]
2. Speed: iOS lands month 9 to 10, inside the approved envelope's buffer, and the paid layer still lands inside the competitive window. The roughly 4 to 6 added person-months is the cheapest Android of any option, and the one-codebase structure keeps every v1.x feature at approved cost, which is where the window battle is actually won. [inferred from section 4]

The strongest evidence for the framework choice, in one line: Runna, the top-rated app in Waypoint's exact category, at millions of users, an Apple App of the Year finalist, ships GPS tracking, adaptive training plans, health and wearable integrations, and RevenueCat subscriptions on iOS AND Android from one React Native codebase with native Swift reserved only for the Watch app. [verified, Runna engineering postings cited in section 1.3] Flutter is the named runner-up (Coopah proves the category on it); KMP is rejected at this team size because it still requires two UI layers.

Why not the others, in one line each: A burns the window for revenue that section 1.2 shows barely exists on Android at MVP; B pays most of D's costs but couples the launches for no strategic gain; C is the only option that keeps DEC-006's stack untouched, but it is the most expensive in total and taxes every future feature twice, which is the wrong trade for a solo founder inside a closing window.

### What this changes in the locked decisions

DEC-006 locked the concept, not the implementation stack; the concept (constraint-based generation, safety-aware routing, HealthKit-first data posture, privacy architecture) is untouched. What changes sits in the approved-but-unlocked Phase 5 stack and scope documents, and one DEC-006 clause:

| Locked or approved item | Status under Option D |
|---|---|
| DEC-006 concept, positioning, NOT list | Unchanged |
| DEC-006 section 6 sequence ("iOS English-first, then Android") | AMENDED: Android moves from v2+ business decision to MVP-era fast-follow (4 to 8 week stagger). Requires a new decision record (next DEC number) since concept changes require one. |
| `mvp-scope.md` ~25 pm / 8 to 10 months | AMENDED: ~29 to 31 pm; iOS month 9 to 10; Android month 10 to 12. The 15-feature list itself is unchanged on both platforms. |
| SwiftUI client | REPLACED by React Native (TypeScript), native modules where needed (Foundation Models, WorkoutKit, HealthKit bridges) |
| MapKit | REPLACED by MapLibre Native on both platforms (parity, Ferrostar alignment, zero usage fees) |
| Apple Foundation Models coaching layer | KEPT on capable iPhones via a native module; template fallback is primary on Android (ML Kit GenAI polish on capable flagships only); health data stays on-device on both platforms |
| GraphHopper, Supabase, Hetzner, RevenueCat, WeatherKit-plus-fallback | Unchanged (backend is platform-independent; RevenueCat's RN SDK covers Play Billing; Android weather calls route through the server-side Open-Meteo fallback already planned) |
| Hiring profile | Senior iOS contractor becomes senior React Native contractor with native iOS/Android module experience |

### The founder decision, framed cleanly

Three choices, one recommended:

1. **RECOMMENDED. Staged cross-platform (Option D):** React Native, one codebase, iOS month 9 to 10, Android 4 to 8 weeks later. Cost: roughly +4 to 6 pm, a stack amendment recorded as a new DEC, and accepting framework dependency in exchange for permanent one-codebase economics. Choose this if both goals (coverage and speed) are genuinely non-negotiable.
2. **Staged native (Option C):** keep every approved stack choice; add an Android team at month 5; Android ships within 3 to 4 months of iOS. Cost: roughly +13 to 15 pm, +1.5 to 2 FTE of burn, and a permanent two-codebase tax on the roadmap. Choose this if native polish on both platforms outweighs cost and roadmap speed, or if the founder distrusts framework dependency more than double maintenance.
3. **Challenge the requirement (approved plan, Android in v1.x):** the evidence honestly supports launching iOS-only and starting the Android build (Option D's codebase would make even this cheap) after week-4 retention is proven, since Android carries roughly 15 percent of category subscription revenue and every competitor that won staged its launch. Choose this if, seeing the numbers, "both platforms at MVP" softens to "both platforms within the first year".

What is NOT on the menu: Option A. Simultaneous dual-native puts the launch at month 11 to 13 and the paid layer at the window's edge; it is the one option this analysis flags as endangering the business premise, and no competitor precedent supports it.

Decision needed from Claudio: pick 1, 2, or 3. If 1 or 2, a new decision record amending DEC-006's sequencing clause (and, for choice 1, the stack) must be written before build start, and `mvp-scope.md` plus `stack-recommendation.md` get amendment notes. The month-1 Ferrostar spike (already mandatory) expands to a dual-platform spike under choices 1 and 2: it must return a verdict on guidance-engine architecture for both platforms.

## Assumptions

- A14: The client/backend effort decomposition of the approved 22.75 pm (roughly 13 to 14 pm client, 9 to 10 pm platform-independent) is a planning estimate derived from the per-feature table in `mvp-scope.md`, not a measured split.
- A15: All option-level person-month and calendar figures are planning estimates built from the A14 decomposition plus researched platform deltas; the walking-skeleton build is the calibration instrument, as in the approved plan.
- A16: Runna's exact Android general-availability date is not published; its Google Play listing and React Native architecture support "both platforms from early on" but not a verified day-zero simultaneous launch.
- A17: The 12 to 18 month Strava window (from `positioning.md`) is carried forward unchanged; all window-impact verdicts inherit it.
- A18: Framework adoption percentages (RN 35 to 43 percent, Flutter 35 to 46 percent, KMP 23 percent) vary across the surveyed sources; this analysis relies only on their direction (all three mainstream, KMP fastest-growing), not their precision.
- A19: The assumption that Waypoint's target runner segment skews premium-device (raising effective iOS share and, on Android, flagship share for ML Kit GenAI coverage) remains unproven until onboarding telemetry exists (extends A12 from `stack-validation.md`).

## Open questions

- Does Garmin Connect write workouts, heart rate, and the signals Waypoint needs into Health Connect in 2026? This is the H6 verification gap for Android and the highest-priority follow-up before any Android commitment is finalized. #open-question
- Ferrostar under React Native: are the in-progress RN bindings usable, or does the guidance engine live in shared TypeScript with thin native TTS/location modules? Expanded month-1 spike deliverable. #open-question
- Expo managed workflow vs bare workflow given the native modules required (Foundation Models, WorkoutKit, background geolocation SDK). Spike-adjacent decision. #open-question
- transistorsoft background-geolocation license cost and terms for production (license required for release builds); price not captured this pass. #open-question
- Android beta hardware matrix: which Samsung and Xiaomi devices, and does the beta program need EU devices for OEM-killer coverage? Decide with the launch-metro decision. #open-question
- If choice 3 (challenge the requirement) is taken, does the React Native rebase still pay for itself as Android insurance? Directionally yes (it converts a future Android build into a certification exercise), but the 0 to 1 month iOS toll must be re-judged against a pure-Swift plan. #open-question

## Related

- `research/05-product/stack-recommendation.md` (the iOS stack this document amends under choices 1 and 2)
- `research/05-product/stack-validation.md` (second-opinion validation; its conditions carry forward unchanged)
- `research/05-product/mvp-scope.md` (the 15-feature MVP and effort baseline)
- `research/04-synthesis/concept.md` (DEC-006; section 6 sequencing clause is the one affected)
- `research/00-RESEARCH-PLAYBOOK.md` (standards followed here)
