#!/usr/bin/env python3
"""Expand awesome-rust README by doubling resource table rows."""

from pathlib import Path

README = Path(__file__).parent / "README.md"

NEW_ROWS = {
    "Official & Docs": [
        '| [The rustc book](https://doc.rust-lang.org/rustc/) | Docs | Advanced | Free | Compiler flags, targets, codegen options, and LTO settings — consult when build configuration affects release binaries. | 🔴 🆓 🌐 |',
        '| [Rustup book](https://rust-lang.github.io/rustup/) | Guide | Beginner | Free | Toolchain installation, components, targets, and overrides — authoritative reference beyond the rustup.rs landing page. | 🟢 🆓 🌐 |',
        '| [Diagnostics reference](https://doc.rust-lang.org/rustc/diagnostics/index.html) | Reference | Intermediate | Free | Catalog of rustc lint groups and diagnostic levels — tune warnings for CI and local development workflows. | 🟡 🆓 🌐 |',
        '| [Attribute reference](https://doc.rust-lang.org/reference/attributes.html) | Reference | Advanced | Free | Every built-in attribute documented — essential when reading derive macros and conditional compilation. | 🔴 🆓 🌐 📘 |',
        '| [Keywords reference](https://doc.rust-lang.org/reference/keywords.html) | Reference | Beginner | Free | Reserved words and raw identifier syntax — quick lookup when naming conflicts with language keywords. | 🟢 🆓 🌐 |',
        '| [Primitive types reference](https://doc.rust-lang.org/reference/types.html#primitive-types) | Reference | Beginner | Free | Fixed-width integers, floats, bool, char, and unit type semantics — baseline for numeric API design. | 🟢 🆓 🌐 |',
        '| [Const evaluation reference](https://doc.rust-lang.org/reference/const_eval.html) | Reference | Advanced | Free | What can run at compile time — unlocks const generics and static initialization patterns. | 🔴 🆓 🌐 📘 |',
        '| [Cargo workspaces guide](https://doc.rust-lang.org/cargo/reference/workspaces.html) | Guide | Intermediate | Free | Multi-crate repository layout and shared dependency versions — structure before monorepos sprawl. | 🟡 🆓 🌐 |',
        '| [Cargo publishing guide](https://doc.rust-lang.org/cargo/reference/publishing.html) | Guide | Intermediate | Free | crates.io publish workflow, API tokens, and yanking — complete the loop from local crate to registry. | 🟡 🆓 🌐 🚀 |',
        '| [Package metadata docs](https://doc.rust-lang.org/cargo/reference/manifest.html#the-package-section) | Reference | Intermediate | Free | Authors, description, keywords, and categories fields — metadata that affects crates.io discoverability. | 🟡 🆓 🌐 |',
        '| [Doctest attributes](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html#attributes) | Docs | Intermediate | Free | `no_run`, `should_panic`, and `ignore` doctest flags — control which examples execute in CI. | 🟡 🆓 🌐 🛠 |',
        '| [Rust test book](https://doc.rust-lang.org/book/ch11-00-testing.html) | Docs | Beginner | Free | Official testing chapter cross-linked from the Book — canonical unit and integration test patterns. | 🟢 🆓 🌐 |',
        '| [Target specification JSON](https://doc.rust-lang.org/nightly/rustc/target-specification.html) | Reference | Advanced | Free | Custom target definitions for embedded and exotic platforms — required for bare-metal cross-compilation. | 🔴 🆓 🌐 📘 |',
        '| [Rustfix book](https://doc.rust-lang.org/nightly/nightly-rustc/rustfix.html) | Guide | Intermediate | Free | Automated migration suggestions from `cargo fix` — apply edition upgrades with less manual editing. | 🟡 🆓 🌐 |',
        '| [Conditional compilation](https://doc.rust-lang.org/reference/conditional-compilation.html) | Reference | Intermediate | Free | `cfg`, `target_os`, and feature gates — platform-specific code without runtime branching overhead. | 🟡 🆓 🌐 📘 |',
        '| [Rust playground source](https://github.com/integer32llc/playground) | Repository | Intermediate | Free | Open-source playground implementation — understand limits and contribute if your demos need custom flags. | 🟡 🆓 📦 |',
        '| [Contributing to Rust](https://github.com/rust-lang/rust/blob/master/CONTRIBUTING.md) | Guide | Advanced | Free | Issue filing, PR workflow, and bootstrap instructions — entry point for rustc and stdlib contributions. | 🔴 🆓 🌐 🚀 |',
        '| [Rust 2024 Edition Guide](https://doc.rust-lang.org/edition-guide/rust-2024/index.html) | Guide | Intermediate | Free | Migration notes for the 2024 edition — read before bumping `edition` in existing codebases. | 🟡 🆓 🌐 |',
        '| [The beta book](https://doc.rust-lang.org/beta/book/) | Book (online) | Beginner | Free | Pre-release Book snapshot — preview upcoming documentation changes before stable release. | 🟢 🆓 🌐 |',
        '| [Nightly std docs](https://doc.rust-lang.org/nightly/std/) | API reference | Advanced | Free | Unstable std APIs and upcoming features — reference when experimenting on nightly toolchains. | 🔴 🆓 🌐 |',
        '| [Rustdoc search index](https://doc.rust-lang.org/rustdoc/read-documentation/search.html) | Docs | Intermediate | Free | How rustdoc builds search indexes — configure crate docs for better on-site navigation. | 🟡 🆓 🌐 |',
        '| [Linking chapter (Reference)](https://doc.rust-lang.org/reference/linkage.html) | Reference | Advanced | Free | Static vs dynamic linking, `#[link]`, and native library dependencies — FFI build troubleshooting. | 🔴 🆓 🌐 📘 |',
        '| [Type layout reference](https://doc.rust-lang.org/reference/type-layout.html) | Reference | Advanced | Free | Size, alignment, and repr attributes — critical for FFI structs and embedded memory maps. | 🔴 🆓 🌐 📘 |',
        '| [Rustdoc intra-doc links](https://doc.rust-lang.org/rustdoc/write-documentation/linking-to-items-by-name.html) | Docs | Intermediate | Free | Cross-link types within crate documentation — keeps docs.rs navigation cohesive without hardcoded URLs. | 🟡 🆓 🌐 |',
        '| [Cargo environment variables](https://doc.rust-lang.org/cargo/reference/environment-variables.html) | Reference | Intermediate | Free | `CARGO_TARGET_DIR`, `RUSTFLAGS`, and profile overrides — CI and local build customization. | 🟡 🆓 🌐 |',
        '| [Profiles reference](https://doc.rust-lang.org/cargo/reference/profiles.html) | Reference | Intermediate | Free | dev, release, bench, and custom profile tuning — control optimization and debug info per build mode. | 🟡 🆓 🌐 |',
        '| [Rust analyzer manual](https://rust-analyzer.github.io/manual.html) | Guide | Intermediate | Free | Configuration, flycheck, and proc-macro settings — tune IDE behavior beyond default VS Code setup. | 🟡 🆓 🌐 |',
        '| [Rust changelog](https://github.com/rust-lang/rust/blob/master/RELEASES.md) | Reference | Intermediate | Free | Complete stable release changelog — grep for breaking changes before toolchain upgrades. | 🟡 🆓 🌐 |',
        '| [The FFI chapter (Nomicon)](https://doc.rust-lang.org/nomicon/ffi.html) | Docs | Advanced | Free | Cross-reference from official docs for FFI safety — pairs with bindgen and cxx workflows. | 🔴 🆓 🌐 📘 |',
        '| [Rustdoc lints](https://doc.rust-lang.org/rustdoc/lints.html) | Docs | Intermediate | Free | Documentation quality lints like broken links and missing docs — enforce API documentation standards in CI. | 🟡 🆓 🌐 ✅ |',
        '| [Module path resolution](https://doc.rust-lang.org/reference/items/modules.html) | Reference | Intermediate | Free | How `mod` paths resolve across files — debug confusing module not found errors in larger crates. | 🟡 🆓 🌐 📘 |',
        '| [Rust playground integration](https://doc.rust-lang.org/rustdoc/write-documentation/link-to-rust-playground.html) | Docs | Intermediate | Free | Add runnable playground buttons to rustdoc pages — lowers barrier for users trying your API examples. | 🟡 🆓 🌐 🛠 |',
    ],
    "Beginner": [
        '| [Rust Book translations index](https://github.com/rust-lang/book/tree/main/translations) | Book | Beginner | Free | Community translations of the official Book — learn in your native language when available. | 🟢 🆓 🌐 |',
        '| [Rustfinity beginner path](https://www.rustfinity.com/learn) | Exercises | Beginner | Freemium | Browser-based progressive exercises — gamified syntax drills before local toolchain setup. | 🟢 🆓 💰 🛠 |',
        '| [Programming Rust examples repo](https://github.com/ProgrammingRust/examples) | Exercises | Intermediate | Free | Companion code for the O\'Reilly book — runnable samples extending Book concepts with production patterns. | 🟡 🆓 📦 🛠 |',
        '| [Rustlings unofficial solutions (after attempt)](https://github.com/rust-lang/rustlings#solutions) | Community | Beginner | Free | Official guidance on when and how to check solutions — preserves learning discipline during drills. | 🟢 🆓 📦 |',
        '| [Rust Book Mermaid diagrams](https://github.com/rust-lang/book) | Book | Beginner | Free | Visual chapter diagrams in the Book source — supplementary mental models for ownership flow. | 🟢 🆓 📦 |',
        '| [Rustlings install guide](https://github.com/rust-lang/rustlings#getting-started) | Docs | Beginner | Free | Step-by-step setup including rustup verification — first command sequence after toolchain install. | 🟢 🆓 🌐 🛠 |',
        '| [Rust Playground share links](https://play.rust-lang.org/) | Tool | Beginner | Free | Generate shareable URLs for code snippets — ask for help in forums with reproducible examples. | 🟢 🆓 🌐 🛠 |',
        '| [Rust Book chapter exercises](https://github.com/rust-lang/book/tree/main/listings) | Exercises | Beginner | Free | Official listing source code from each Book chapter — compare your solutions against canonical versions. | 🟢 🆓 📦 🛠 |',
        '| [Rustlings watch mode](https://github.com/rust-lang/rustlings#doing-rustlings) | Tool | Beginner | Free | Auto-rerun on file save during exercises — tight feedback loop while learning ownership rules. | 🟢 🆓 📦 🛠 |',
        '| [Rust Book audio community project](https://github.com/rust-lang/book) | Book | Beginner | Free | Community efforts to narrate Book chapters — alternative learning modality for commute time. | 🟢 🆓 📦 |',
        '| [Rust Study (Discord study group)](https://github.com/ryanmcgrath/rust-study) | Community | Beginner | Free | Structured group learning schedules — accountability partners for the first ownership plateau. | 🟢 🆓 📦 🛠 |',
        '| [Rustlings force mode](https://github.com/rust-lang/rustlings#forcing-rustlings-to-look-at-the-current-exercise) | Tool | Beginner | Free | Focus on one exercise at a time — prevents skipping ahead when borrow errors feel overwhelming. | 🟢 🆓 📦 |',
        '| [Rust Book playground integration](https://doc.rust-lang.org/book/ch01-02-hello-world.html) | Docs | Beginner | Free | Runnable examples embedded in early chapters — experiment with Hello World variants in-browser. | 🟢 🆓 🌐 🛠 |',
        '| [Rust Book quiz (community)](https://github.com/pretzelhammer/rust-blog/blob/master/posts/common-rust-traps.md) | Article | Beginner | Free | Common traps for newcomers — read after Book ch. 4 to avoid predictable ownership mistakes. | 🟢 🆓 📘 |',
        '| [Rust Book Spanish translation](https://github.com/rust-lang/book/tree/main/translations/es) | Book | Beginner | Free | Spanish edition of the official Book — high-quality community translation maintained with upstream. | 🟢 🆓 🌐 |',
        '| [Rust Book Chinese translation](https://github.com/KaiserY/trpl-zh-cn) | Book | Beginner | Free | Widely used Chinese translation of the Book — large community maintaining chapter parity with stable. | 🟢 🆓 📦 |',
        '| [Rust Book Japanese translation](https://github.com/rust-lang-ja/book-ja) | Book | Beginner | Free | Official Japanese Book translation project — maintained alongside English edition updates. | 🟢 🆓 🌐 |',
        '| [Rust Book Korean translation](https://github.com/rinthel/rust-lang-book-ko) | Book | Beginner | Free | Korean community translation — chapter coverage for native Korean speakers starting Rust. | 🟢 🆓 📦 |',
        '| [Rust Book French translation](https://github.com/Jimskapt/rust-book-fr) | Book | Beginner | Free | French community translation — alternative narrative voice for francophone learners. | 🟢 🆓 📦 |',
        '| [Rust Book Portuguese translation](https://github.com/rust-lang-pt/rustbook-pt-br) | Book | Beginner | Free | Brazilian Portuguese Book translation — maintained by the Rust Brazil community. | 🟢 🆓 📦 |',
        '| [Rust Book Russian translation](https://github.com/ruRust/rust_book_ru) | Book | Beginner | Free | Russian community translation — extensive chapter coverage for Eastern European learners. | 🟢 🆓 📦 |',
        '| [Rust Book Vietnamese translation](https://github.com/rust-lang-vn/book) | Book | Beginner | Free | Vietnamese community Book project — growing chapter set for Southeast Asian developers. | 🟢 🆓 📦 |',
        '| [Rust Book German translation](https://github.com/rust-lang-de/rustbook-de) | Book | Beginner | Free | German community translation — DACH region learners preferring native-language explanations. | 🟢 🆓 📦 |',
        '| [Rust Book Italian translation](https://github.com/rust-lang-it/rustbook-it) | Book | Beginner | Free | Italian community translation — supplementary voice alongside the official English Book. | 🟢 🆓 📦 |',
    ],
    "Intermediate": [
        '| [Rustdoc book — documentation tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) | Docs | Intermediate | Free | Keep public API examples executable — doctest failures catch documentation drift before users do. | 🟡 🆓 🌐 🛠 |',
        '| [Cargo features guide](https://doc.rust-lang.org/cargo/reference/features.html) | Docs | Intermediate | Free | Optional dependencies and feature unification — prevent surprise feature leakage across workspace members. | 🟡 🆓 🌐 |',
        '| [Rust I/O chapter (Book ch. 12)](https://doc.rust-lang.org/book/ch12-00-an-io-project.html) | Docs | Intermediate | Free | File I/O project building a CLI tool — bridges fundamentals to real command-line programs. | 🟡 🆓 🌐 🛠 |',
        '| [Concurrency chapter (Book ch. 16)](https://doc.rust-lang.org/book/ch16-00-concurrency.html) | Docs | Intermediate | Free | Threads, channels, and shared-state patterns — foundation before async runtimes. | 🟡 🆓 🌐 📘 |',
        '| [OOP chapter (Book ch. 17)](https://doc.rust-lang.org/book/ch17-00-oop.html) | Docs | Intermediate | Free | Traits, trait objects, and state patterns — Rust\'s answer to classical OOP without inheritance. | 🟡 🆓 🌐 📘 |',
        '| [Patterns chapter (Book ch. 18)](https://doc.rust-lang.org/book/ch18-00-patterns.html) | Docs | Intermediate | Free | Refutability, `@` bindings, and match guards — write exhaustive domain logic safely. | 🟡 🆓 🌐 |',
        '| [env_logger crate](https://docs.rs/env_logger/) | Library | Intermediate | Open Source | Simple logging initialization from environment variables — quick setup before adopting tracing. | 🟡 📦 |',
        '| [log crate](https://docs.rs/log/) | Library | Intermediate | Open Source | Facade logging trait used across the ecosystem — abstraction layer beneath tracing and env_logger. | 🟡 📦 🔥 |',
        '| [uuid crate](https://docs.rs/uuid/) | Library | Intermediate | Open Source | Standard UUID generation and parsing — appears in nearly every API and database schema layer. | 🟡 📦 |',
        '| [chrono crate](https://docs.rs/chrono/) | Library | Intermediate | Open Source | Date and time handling for applications — pair with time crate for newer timezone-aware APIs. | 🟡 📦 🔥 |',
        '| [time crate](https://docs.rs/time/) | Library | Intermediate | Open Source | Modern date-time library with const-friendly APIs — preferred for new projects avoiding chrono legacy. | 🟡 📦 |',
        '| [regex crate](https://docs.rs/regex/) | Library | Intermediate | Open Source | Official regular expression engine — linear-time matching safe for untrusted input patterns. | 🟡 📦 🔥 |',
        '| [url crate](https://docs.rs/url/) | Library | Intermediate | Free | URL parsing and manipulation — standard for HTTP clients and web frameworks handling user input. | 🟡 🆓 📦 |',
        '| [indexmap crate](https://docs.rs/indexmap/) | Library | Intermediate | Open Source | Insertion-ordered HashMap — preserves key order for config files and deterministic serialization. | 🟡 📦 |',
        '| [dashmap crate](https://docs.rs/dashmap/) | Library | Intermediate | Open Source | Concurrent HashMap without global locks — shared caches in multi-threaded servers. | 🟡 📦 |',
        '| [parking_lot crate](https://docs.rs/parking_lot/) | Library | Intermediate | Open Source | Faster Mutex and RwLock implementations — drop-in replacement when std locks profile hot. | 🟡 📦 |',
        '| [once_cell / std OnceLock](https://doc.rust-lang.org/std/sync/struct.OnceLock.html) | Library | Intermediate | Free | Lazy static initialization in stable Rust — replaces lazy_static for global singletons. | 🟡 🆓 🌐 |',
        '| [derive_more crate](https://docs.rs/derive_more/) | Library | Intermediate | Open Source | Additional derive macros for From, Display, and operator traits — reduces boilerplate in domain types. | 🟡 📦 |',
        '| [strum crate](https://docs.rs/strum/) | Library | Intermediate | Open Source | Enum string conversion and iteration derives — clean Display and FromStr for configuration enums. | 🟡 📦 |',
        '| [config crate](https://docs.rs/config/) | Library | Intermediate | Open Source | Layered configuration from files, env, and defaults — standard pattern for twelve-factor Rust services. | 🟡 📦 |',
        '| [dotenvy crate](https://docs.rs/dotenvy/) | Library | Intermediate | Open Source | Load `.env` files for local development — keeps secrets out of source while matching production env vars. | 🟡 📦 |',
        '| [validator crate](https://docs.rs/validator/) | Library | Intermediate | Open Source | Declarative field validation derives — input validation without hand-written match chains. | 🟡 📦 |',
        '| [async-trait crate](https://docs.rs/async-trait/) | Library | Intermediate | Open Source | Async methods in traits via macro desugaring — pragmatic workaround until native async traits stabilize. | 🟡 📦 🔥 |',
        '| [tower-http crate](https://docs.rs/tower-http/) | Library | Intermediate | Open Source | HTTP middleware for compression, CORS, and tracing — standard Axum service layer additions. | 🟡 📦 🔥 |',
    ],
    "Advanced": [
        '| [miniz_oxide / flate2](https://docs.rs/flate2/) | Library | Advanced | Open Source | Compression and decompression — binary format parsers and HTTP middleware depend on these primitives. | 🔴 📦 |',
        '| [syn crate](https://docs.rs/syn/) | Library | Advanced | Open Source | Rust syntax parser for proc-macro authoring — foundation of the derive macro ecosystem. | 🔴 📦 📘 ⭐ |',
        '| [quote crate](https://docs.rs/quote/) | Library | Advanced | Open Source | Quasi-quoting for proc macros — pairs with syn to generate Rust code at compile time. | 🔴 📦 📘 |',
        '| [proc-macro2 crate](https://docs.rs/proc-macro2/) | Library | Advanced | Open Source | Proc-macro API usable in unit tests — test macro expansions without separate proc-macro crates. | 🔴 📦 📘 |',
        '| [wasm-bindgen guide](https://rustwasm.github.io/wasm-bindgen/) | Guide | Advanced | Free | JavaScript interop for WASM modules — bridge browser APIs from compiled Rust. | 🔴 🆓 🌐 🚀 |',
        '| [wasm-pack book](https://rustwasm.github.io/docs/wasm-pack/) | Guide | Intermediate | Free | Build and publish WASM packages to npm — packaging workflow beyond raw wasm32 compilation. | 🟡 🆓 🌐 🚀 |',
        '| [Rust embedded discovery](https://docs.rust-embedded.org/discovery/) | Book (online) | Advanced | Free | Hands-on embedded tutorial with STM32 — step-by-step firmware before reading the full Embedded Book. | 🔴 🆓 🌐 🛠 |',
        '| [The Redox Book](https://doc.redox-os.org/book/) | Book (online) | Advanced | Free | Rust-native operating system documentation — see ownership and no_std applied to kernel design. | 🔴 🆓 📘 |',
        '| [Rust kernel module guide](https://rust-for-linux.com/) | Guide | Advanced | Free | Linux kernel Rust integration patterns — case study for unsafe boundaries at OS scale. | 🔴 🆓 📘 |',
        '| [Stacked Borrows (Miri)](https://github.com/rust-lang/miri/blob/master/BORROWCK.md) | Reference | Advanced | Free | Formal model Miri uses for aliasing — understand why some unsafe patterns fail Miri checks. | 🔴 🆓 📘 |',
        '| [Rust verification workshop](https://model-checking.github.io/kani/) | Guide | Advanced | Free | Kani model-checking tutorials — prove properties on bounded code beyond Miri sampling. | 🔴 🆓 📘 |',
        '| [cbindgen](https://github.com/mozilla/cbindgen) | Tool | Advanced | Open Source | Generate C headers from Rust FFI exports — automate header sync when exposing C-compatible APIs. | 🔴 📦 🛠 |',
        '| [safer_ffi crate](https://docs.rs/safer_ffi/) | Library | Advanced | Open Source | Safer FFI boundary abstractions — reduce hand-written unsafe in cross-language interfaces. | 🔴 📦 📘 |',
        '| [bytemuck crate](https://docs.rs/bytemuck/) | Library | Advanced | Open Source | Safe transmute patterns for plain data types — graphics and embedded code casting byte buffers. | 🔴 📦 📘 |',
        '| [zerocopy crate](https://docs.rs/zerocopy/) | Library | Advanced | Open Source | Zero-copy parsing of packed structs — network protocols and binary formats without memcpy overhead. | 🔴 📦 📘 |',
        '| [portable-simd](https://doc.rust-lang.org/core/core_arch/) | Docs | Advanced | Free | Portable SIMD intrinsics in core::simd — vectorize hot loops without platform-specific assembly. | 🔴 🆓 🌐 ⚡ |',
        '| [loom concurrency testing](https://docs.rs/loom/) | Library | Advanced | Open Source | Exhaustive exploration of concurrent interleavings — test async and threaded code for race conditions. | 🔴 📦 🛠 |',
        '| [crossbeam-epoch](https://docs.rs/crossbeam-epoch/) | Library | Advanced | Open Source | Epoch-based memory reclamation — building block for lock-free data structures. | 🔴 📦 📘 |',
        '| [rustc_codegen_cranelift](https://github.com/bjorn3/rustc_codegen_cranelift) | Project | Advanced | Open Source | Alternative Cranelift backend for faster debug builds — experimental but useful for compile-time iteration. | 🔴 📦 |',
        '| [Rust compiler perf site](https://perf.rust-lang.org/) | Tool | Advanced | Free | Track rustc benchmark regressions — context when discussing compile-time improvements upstream. | 🔴 🆓 🌐 |',
    ],
    "Ecosystem & Tools": [
        '| [fd (find alternative)](https://github.com/sharkdp/fd) | CLI tool | Beginner | Open Source | Fast user-friendly find — study alongside ripgrep for polished Rust CLI design patterns. | 🟢 📦 |',
        '| [bat (cat alternative)](https://github.com/sharkdp/bat) | CLI tool | Beginner | Open Source | Syntax-highlighting cat replacement — exemplar of Rust terminal UX with Clap and syntect. | 🟢 📦 🔥 |',
        '| [tokei](https://github.com/XAMPPRocky/tokei) | CLI tool | Intermediate | Open Source | Fast code line counter — useful for portfolio metrics and CI statistics. | 🟡 📦 |',
        '| [starship](https://starship.rs/) | CLI tool | Beginner | Open Source | Cross-shell prompt written in Rust — fast startup and modular configuration. | 🟢 📦 🔥 |',
        '| [bottom (btm)](https://github.com/ClementTsang/bottom) | CLI tool | Intermediate | Open Source | Graphical system monitor for terminals — alternative to htop with customizable widgets. | 🟡 📦 |',
        '| [exa / eza](https://github.com/eza-community/eza) | CLI tool | Beginner | Open Source | Modern ls replacement with icons and git integration — polished file listing UX. | 🟢 📦 |',
        '| [tealdeer (tldr)](https://github.com/tealdeer-rs/tealdeer) | CLI tool | Beginner | Open Source | Simplified man pages client — fast Rust CLI fetching community command examples. | 🟢 📦 |',
        '| [sd (sed alternative)](https://github.com/chmln/sd) | CLI tool | Intermediate | Open Source | Intuitive find-and-replace — regex and literal modes for batch text transformation. | 🟡 📦 |',
        '| [dust (du alternative)](https://github.com/bootandy/dust) | CLI tool | Beginner | Open Source | Intuitive disk usage visualizer — tree-style output for quick storage audits. | 🟢 📦 |',
        '| [procs](https://github.com/dalance/procs) | CLI tool | Intermediate | Open Source | Modern ps replacement with color and filtering — process inspection for debugging services. | 🟡 📦 |',
        '| [bandwhich](https://github.com/imsnif/bandwhich) | CLI tool | Intermediate | Open Source | Terminal bandwidth monitor — identify network-heavy processes without GUI tools. | 🟡 📦 |',
        '| [git-delta](https://github.com/dandavison/delta) | Dev tool | Intermediate | Open Source | Syntax-highlighting git diff pager — already popular; study for terminal rendering patterns. | 🟡 📦 |',
        '| [cargo-generate](https://github.com/cargo-generate/cargo-generate) | Cargo plugin | Intermediate | Open Source | Scaffold projects from git templates — standardize team project boilerplate. | 🟡 📦 🛠 |',
        '| [cargo-make](https://github.com/sagiegurari/cargo-make) | Task runner | Intermediate | Open Source | Task runner defined in TOML — alternative to just for complex multi-step CI workflows. | 🟡 📦 |',
        '| [cargo-release](https://github.com/crate-ci/cargo-release) | Cargo plugin | Intermediate | Open Source | Automated version bumps, changelog, and publish — semver releases with less manual steps. | 🟡 📦 🚀 |',
        '| [cargo-hack](https://github.com/taiki-e/cargo-hack) | Cargo plugin | Advanced | Open Source | Test all feature combinations — catch feature-gate compilation failures before users do. | 🔴 📦 🛠 |',
        '| [cargo-llvm-lines](https://github.com/dtolnay/cargo-llvm-lines) | Analysis tool | Advanced | Open Source | Count LLVM IR lines per function — identify monomorphization bloat causing slow builds. | 🔴 📦 |',
        '| [cargo-bloat (analysis)](https://github.com/RazrFalcon/cargo-bloat) | Analysis tool | Advanced | Open Source | Binary size attribution per crate — trim dependencies before embedded or WASM deployments. | 🔴 📦 |',
        '| [cargo-msrv](https://github.com/foresterre/cargo-msrv) | Cargo plugin | Intermediate | Open Source | Find minimum supported Rust version — document MSRV for library crates accurately. | 🟡 📦 ✅ |',
        '| [cargo-deny (licenses)](https://embarkstudios.github.io/cargo-deny/) | Docs | Intermediate | Free | Configuration reference for license and advisory policies — tune deny.toml for corporate compliance. | 🟡 🆓 🌐 |',
        '| [cargo-audit (RustSec)](https://rustsec.org/) | Organization | Intermediate | Free | Advisory database homepage — subscribe to notifications for crates your services depend on. | 🟡 🆓 🌐 ✅ |',
        '| [crates.io API docs](https://crates.io/data-access) | Reference | Intermediate | Free | Programmatic access to crate metadata — build internal dashboards or dependency analysis tools. | 🟡 🆓 🌐 |',
        '| [lib.rs (crate discovery)](https://lib.rs/) | Registry | Intermediate | Free | Alternative crates.io frontend with better search — discover crates by category and popularity. | 🟡 🆓 🔥 |',
        '| [deps.rs](https://deps.rs/) | Tool | Intermediate | Free | Dependency freshness dashboard for GitHub repos — quick health check on stale dependencies. | 🟡 🆓 |',
        '| [Rust Search Extension](https://rust.extension.js.org/) | Browser tool | Beginner | Free | Browser extension for std and crates.io search — jump to docs.rs from the address bar. | 🟢 🆓 🛠 |',
        '| [crates.io reverse dependencies](https://crates.io/crates/SERDE/reverse_dependencies) | Reference | Intermediate | Free | See who depends on a crate — gauge ecosystem impact before making breaking API changes. | 🟡 🆓 🌐 |',
        '| [cargo-insta review](https://insta.rs/) | Tool | Intermediate | Free | Snapshot test review workflow — accept or reject snapshot diffs from the command line. | 🟡 🆓 🛠 |',
        '| [mold linker docs](https://github.com/rui314/mold#how-to-build) | Docs | Advanced | Free | Installation and Cargo configuration for mold — one-time setup cutting link times dramatically. | 🔴 🆓 📦 |',
        '| [sccache docs](https://github.com/mozilla/sccache#usage) | Docs | Advanced | Free | S3 and Redis backend configuration — share compilation cache across team CI runners. | 🔴 🆓 📦 |',
        '| [rustfilt](https://github.com/luser/rustfilt) | Dev tool | Intermediate | Open Source | Demangle Rust symbol names in stack traces — essential when reading raw backtraces from production. | 🟡 📦 🛠 |',
        '| [backtrace crate](https://docs.rs/backtrace/) | Library | Intermediate | Open Source | Capture stack traces in Rust binaries — integrate with error reporting for production diagnostics. | 🟡 📦 |',
        '| [tracing-subscriber](https://docs.rs/tracing-subscriber/) | Library | Intermediate | Open Source | Logging and tracing output formatting — env-filter and JSON layers for production observability. | 🟡 📦 🔥 |',
    ],
    "Frameworks": [
        '| [Actix actors](https://actix.rs/docs/actix/) | Library | Advanced | Open Source | Actor model underlying Actix Web — understand when actor patterns fit concurrent state machines. | 🔴 📦 📘 |',
        '| [Rocket guide](https://rocket.rs/guide/) | Guide | Intermediate | Free | Official Rocket tutorial and API reference — approachable routing and request guard patterns. | 🟡 🆓 🌐 |',
        '| [Axum examples repo](https://github.com/tokio-rs/axum/tree/main/examples) | Examples | Intermediate | Free | Official example collection — copy patterns for WebSockets, SSE, and middleware layers. | 🟡 🆓 📦 🛠 |',
        '| [Tokio mini-redis example](https://github.com/tokio-rs/mini-redis) | Example | Advanced | Free | Reference Redis-like server from the Tokio team — study concurrent connection handling patterns. | 🔴 🆓 📦 📘 |',
        '| [hyperium/hyper examples](https://github.com/hyperium/hyper/tree/master/examples) | Examples | Advanced | Free | Low-level HTTP server and client samples — foundation beneath Axum and reqwest. | 🔴 🆓 📦 |',
        '| [tonic examples](https://github.com/hyperium/tonic/tree/master/examples) | Examples | Intermediate | Free | gRPC streaming and interceptor patterns — production microservice starting points. | 🟡 🆓 📦 🛠 |',
        '| [Leptos book](https://book.leptos.dev/) | Book (online) | Intermediate | Free | Official Leptos guide for full-stack Rust — reactive UI with server functions. | 🟡 🆓 🌐 🚀 |',
        '| [Yew docs](https://yew.rs/docs) | Docs | Intermediate | Free | Component lifecycle and router documentation — WASM frontend patterns with Rust-only logic. | 🟡 🆓 🌐 🚀 |',
        '| [Dioxus guide](https://dioxuslabs.com/learn/0.5/) | Guide | Intermediate | Free | Cross-platform UI with React-like components — web, desktop, and mobile from one codebase. | 🟡 🆓 🌐 🚀 |',
        '| [Tauri v2 docs](https://v2.tauri.app/) | Docs | Intermediate | Free | Desktop app security model and IPC — lightweight alternative to Electron with Rust backends. | 🟡 🆓 🌐 🚀 |',
        '| [SeaORM docs](https://www.sea-ql.org/SeaORM/docs/) | Docs | Intermediate | Free | Async ORM tutorial and relation patterns — active-record style for Axum stacks. | 🟡 🆓 🌐 |',
        '| [Diesel getting started](https://diesel.rs/guides/getting-started) | Guide | Intermediate | Free | Schema migrations and query builder introduction — type-safe SQL without raw string queries. | 🟡 🆓 🌐 |',
        '| [SQLx offline mode](https://github.com/launchbadge/sqlx/blob/main/OFFLINE.md) | Docs | Intermediate | Free | Compile-time query checking without live database — CI-friendly SQLx workflow. | 🟡 🆓 📦 |',
        '| [Poem OpenAPI](https://docs.rs/poem-openapi/) | Library | Intermediate | Open Source | Auto-generated OpenAPI from handler types — schema-first APIs with minimal boilerplate. | 🟡 📦 |',
        '| [GraphQL async-graphql examples](https://github.com/async-graphql/examples) | Examples | Intermediate | Free | Schema and subscription samples — real-time GraphQL patterns with Axum integration. | 🟡 🆓 📦 |',
        '| [pingora docs](https://github.com/cloudflare/pingora/tree/main/docs) | Docs | Advanced | Free | Cloudflare proxy framework documentation — high-throughput HTTP caching and load balancing. | 🔴 🆓 📦 🔥 |',
        '| [fluvio docs](https://www.fluvio.io/docs/) | Docs | Advanced | Free | Rust-native streaming platform — event pipelines beyond simple message queues. | 🔴 🆓 📘 |',
        '| [bevy book](https://bevyengine.org/learn/book/introduction/) | Book (online) | Intermediate | Free | Official Bevy game engine tutorial — ECS patterns and asset pipeline fundamentals. | 🟡 🆓 🌐 🚀 |',
        '| [egui docs](https://docs.rs/egui/latest/egui/) | Docs | Intermediate | Free | Immediate-mode GUI API reference — rapid tooling UIs without web frontend complexity. | 🟡 🆓 🌐 |',
        '| [iced book](https://book.iced.rs/) | Book (online) | Intermediate | Free | Elm-inspired GUI tutorial — declarative state management for cross-platform desktop apps. | 🟡 🆓 🌐 🚀 |',
        '| [socketioxide examples](https://github.com/Totodore/socketioxide/tree/main/examples) | Examples | Intermediate | Free | Socket.IO integration with Axum — real-time apps with fallback transports. | 🟡 🆓 📦 |',
        '| [ntex docs](https://ntex.rs/) | Docs | Intermediate | Free | Actix-fork framework API — evaluate when comparing Actix alternatives with active maintenance. | 🟡 🆓 🌐 |',
        '| [surrealdb docs](https://surrealdb.com/docs) | Docs | Intermediate | Free | Multi-model database query language — document-graph storage from Axum services. | 🟡 🆓 🌐 |',
        '| [gotham docs](https://gotham.rs/documentation/) | Docs | Intermediate | Free | Middleware-centric HTTP framework — typed state patterns for stateful web apps. | 🟡 🆓 🌐 |',
        '| [rmcp (MCP server)](https://github.com/modelcontextprotocol/rust-sdk) | Library | Intermediate | Open Source | Rust SDK for Model Context Protocol servers — integrate AI tooling with typed Rust backends. | 🟡 📦 |',
        '| [loco.rs](https://loco.rs/) | Web framework | Intermediate | Open Source | Rails-inspired Rust framework with batteries included — migrations, mailers, and background jobs. | 🟡 📦 🚀 🔥 |',
        '| [shuttle](https://www.shuttle.rs/) | Platform | Intermediate | Freemium | Deploy Rust web apps with minimal config — fast path from Axum prototype to hosted service. | 🟡 🆓 💰 🚀 |',
        '| [spin (Fermyon)](https://developer.fermyon.com/spin/rust-components) | Platform | Intermediate | Free | WebAssembly microservices on Spin — edge deployment for Rust HTTP handlers. | 🟡 🆓 🚀 |',
        '| [worker-rs (Cloudflare)](https://github.com/cloudflare/workers-rs) | Library | Intermediate | Open Source | Cloudflare Workers SDK for Rust — edge compute without managing servers. | 🟡 📦 🚀 |',
        '| [ractor actor framework](https://docs.rs/ractor/) | Library | Advanced | Open Source | Actor framework inspired by Erlang — supervision trees for fault-tolerant concurrent services. | 🔴 📦 📘 |',
        '| [ambassador (derive)](https://docs.rs/ambassador/) | Library | Advanced | Open Source | Delegate trait implementations to inner types — reduce boilerplate in wrapper and proxy patterns. | 🔴 📦 |',
        '| [rmqtt broker](https://github.com/rmqtt/rmqtt) | Application | Advanced | Open Source | Scalable MQTT broker in Rust — IoT messaging at production scale without Erlang dependencies. | 🔴 📦 |',
    ],
    "Testing": [
        '| [cargo test book chapter](https://doc.rust-lang.org/cargo/guide/tests.html) | Docs | Intermediate | Free | Integration test directory layout and dev-dependencies — structure before scaling test suites. | 🟡 🆓 🌐 |',
        '| [libtest_mimic](https://docs.rs/libtest_mimic/) | Library | Intermediate | Open Source | Custom test harness while keeping cargo test UX — multi-configuration integration test runners. | 🟡 📦 |',
        '| [criterion template](https://github.com/bheisler/criterion.rs/tree/master/criterion) | Examples | Advanced | Free | Benchmark harness examples — baseline for statistical performance regression tests. | 🔴 🆓 📦 |',
        '| [googletest-rs](https://docs.rs/googletest/) | Library | Intermediate | Open Source | GoogleTest-style matchers in Rust — expressive assertions for complex structured output. | 🟡 📦 |',
        '| [claim crate](https://docs.rs/claim/) | Library | Intermediate | Open Source | Assert macros with better error messages — clearer failures than raw assert_eq in large structs. | 🟡 📦 |',
        '| [pretty_assertions (dev)](https://docs.rs/pretty_assertions/) | Library | Intermediate | Open Source | Diff-colored assertion output — instantly readable test failures in CI logs. | 🟡 📦 |',
        '| [snapbox](https://docs.rs/snapbox/) | Library | Intermediate | Open Source | CLI output snapshot testing — successor patterns to insta for command-line tools. | 🟡 📦 🛠 |',
        '| [trycmd](https://docs.rs/trycmd/) | Library | Intermediate | Open Source | CLI integration tests from markdown files — document and test CLI behavior in one file. | 🟡 📦 🛠 |',
        '| [dir-test](https://docs.rs/dir-test/) | Library | Intermediate | Open Source | One test per file in a directory — table-driven tests without macro boilerplate. | 🟡 📦 |',
        '| [test-log](https://docs.rs/test-log/) | Library | Intermediate | Open Source | Capture tracing output during tests — debug failing async tests with structured logs. | 🟡 📦 |',
        '| [serial_test crate](https://docs.rs/serial_test/) | Library | Intermediate | Open Source | Force sequential test execution — prevent flaky failures when tests share env vars or files. | 🟡 📦 |',
        '| [temp-env](https://docs.rs/temp-env/) | Library | Intermediate | Open Source | Temporarily set environment variables in tests — RAII cleanup without test pollution. | 🟡 📦 |',
        '| [httpmock](https://docs.rs/httpmock/) | Library | Intermediate | Open Source | HTTP mocking for integration tests — lighter alternative to wiremock for simple stub endpoints. | 🟡 📦 🛠 |',
        '| [mockito](https://docs.rs/mockito/) | Library | Intermediate | Open Source | HTTP mock server for tests — verify outbound requests without hitting real APIs. | 🟡 📦 |',
        '| [axum-test](https://docs.rs/axum-test/) | Library | Intermediate | Open Source | Test Axum routers without binding ports — fast HTTP handler integration tests. | 🟡 📦 🛠 🔥 |',
        '| [tower::ServiceExt testing](https://docs.rs/tower/latest/tower/trait.ServiceExt.html) | Docs | Advanced | Free | Call tower services directly in tests — unit test middleware without HTTP overhead. | 🔴 🆓 🌐 |',
        '| [cargo-nextest docs](https://nexte.st/docs/) | Docs | Intermediate | Free | Configuration, filtering, and CI integration — maximize parallel test throughput. | 🟡 🆓 🌐 |',
        '| [cargo-llvm-cov guide](https://github.com/taiki-e/cargo-llvm-cov#usage) | Docs | Intermediate | Free | Generate lcov and HTML coverage reports — identify untested branches before release. | 🟡 🆓 📦 |',
        '| [mutants.rs guide](https://mutants.rs/getting-started.html) | Guide | Advanced | Free | Mutation testing workflow — find weak tests that pass without asserting real behavior. | 🔴 🆓 📘 |',
        '| [trybuild examples](https://github.com/dtolnay/trybuild) | Examples | Advanced | Free | Compile-fail test patterns for proc macros — assert expected compiler errors in CI. | 🔴 🆓 📦 📘 |',
    ],
    "Performance": [
        '| [Rust perf book — profiling](https://nnethercote.github.io/perf-book/profiling.html) | Book (online) | Advanced | Free | Chapter on profiling workflows — systematic approach before changing hot-path code. | 🔴 🆓 📘 |',
        '| [Rust perf book — heap](https://nnethercote.github.io/perf-book/heap.html) | Book (online) | Advanced | Free | Allocation reduction strategies — eliminate hidden clones and temporary containers. | 🔴 🆓 📘 |',
        '| [perf-event crate](https://docs.rs/perf-event/) | Library | Advanced | Open Source | Linux perf_event bindings — hardware counter access from Rust profiling tools. | 🔴 📦 |',
        '| [inferno crate](https://docs.rs/inferno/) | Library | Advanced | Open Source | Generate flame graphs programmatically — embed profiling visualization in custom tools. | 🔴 📦 |',
        '| [coz profiler](https://github.com/plasma-umass/coz) | Tool | Advanced | Free | Causal profiling for parallelism — find code whose speedup would help most (Rust via FFI). | 🔴 🆓 📘 |',
        '| [valgrind massif](https://valgrind.org/docs/manual/ms-manual.html) | Tool | Advanced | Free | Heap profiler showing allocation peaks — pair with Rust binaries for memory regression tests. | 🔴 🆓 📘 |',
        '| [bytehound allocator](https://github.com/koute/bytehound) | Profiler | Advanced | Open Source | Memory profiler for Rust via LD_PRELOAD — track allocation sites without code changes. | 🔴 📦 🛠 |',
        '| [samply profiler](https://github.com/mstange/samply) | Profiler | Intermediate | Open Source | Cross-platform sampling profiler with Firefox Profiler UI — easy onboarding for CPU profiles. | 🟡 📦 🛠 🔥 |',
        '| [cargo-flamegraph README](https://github.com/flamegraph-rs/flamegraph) | Docs | Advanced | Free | Usage flags and platform notes — quick CPU profiling setup for any Rust binary. | 🔴 🆓 📦 |',
        '| [rustc codegen options](https://doc.rust-lang.org/rustc/codegen-options/index.html) | Reference | Advanced | Free | opt-level, lto, and target-cpu flags — tune release builds for your deployment hardware. | 🔴 🆓 🌐 ⚡ |',
        '| [target-cpu native](https://doc.rust-lang.org/rustc/codegen-options/index.html#target-cpu) | Reference | Advanced | Free | Enable CPU-specific SIMD instructions — measurable wins on known deployment targets. | 🔴 🆓 🌐 ⚡ |',
        '| [bumpalo arena](https://docs.rs/bumpalo/) | Library | Advanced | Open Source | Bump allocator for arena allocation — eliminate allocator overhead in parse-and-discard workloads. | 🔴 📦 📘 |',
        '| [mimalloc allocator](https://docs.rs/mimalloc/) | Library | Advanced | Open Source | High-performance allocator — evaluate when default alloc shows contention under load. | 🔴 📦 |',
        '| [tikv-jemallocator](https://docs.rs/tikv-jemallocator/) | Library | Advanced | Open Source | jemalloc bindings used by TiKV — production-tested allocator for allocation-heavy services. | 🔴 📦 |',
        '| [rustc-hash (FxHash)](https://docs.rs/rustc-hash/) | Library | Intermediate | Open Source | Fast non-cryptographic hasher — faster HashMap for integer and pointer keys. | 🟡 📦 |',
        '| [fxhash crate](https://docs.rs/fxhash/) | Library | Intermediate | Open Source | FxHashMap and FxHashSet — drop-in faster maps when DOS resistance is not required. | 🟡 📦 |',
        '| [memchr crate](https://docs.rs/memchr/) | Library | Intermediate | Open Source | SIMD-accelerated byte search — ripgrep-speed substring finding for parsers and search tools. | 🟡 📦 🔥 |',
        '| [itoa / ryu crates](https://docs.rs/itoa/) | Library | Intermediate | Open Source | Fast integer and float formatting — avoid format! allocation in hot serialization paths. | 🟡 📦 |',
        '| [sonic-rs JSON](https://github.com/cloudwego/sonic-rs) | Library | Advanced | Open Source | High-performance JSON serializer — CloudWeGo\'s Rust port when serde_json bottlenecks. | 🔴 📦 ⚡ |',
        '| [bincode crate](https://docs.rs/bincode/) | Library | Intermediate | Open Source | Compact binary serialization — faster than JSON for internal service communication. | 🟡 📦 |',
        '| [rkyv zero-copy](https://rkyv.org/) | Library | Advanced | Open Source | Zero-copy deserialization framework — mmap-friendly data formats for extreme read performance. | 🔴 📦 📘 |',
        '| [polars (performance)](https://docs.rs/polars/) | Library | Advanced | Open Source | DataFrame library with lazy evaluation — columnar processing faster than row-by-row iteration. | 🔴 📦 ⚡ 🔥 |',
        '| [arrow-rs](https://docs.rs/arrow/) | Library | Advanced | Open Source | Apache Arrow columnar format — interop with Parquet and data pipelines at scale. | 🔴 📦 📘 |',
        '| [linfa ML crate](https://docs.rs/linfa/) | Library | Advanced | Open Source | Rust-native machine learning toolkit — ndarray-based algorithms without Python overhead. | 🔴 📦 |',
    ],
    "Security": [
        '| [RustSec working group](https://github.com/RustSec) | Organization | Intermediate | Free | Maintainers of advisory-db and cargo-audit — central hub for Rust supply-chain security. | 🟡 🆓 🌐 ⭐ |',
        '| [advisory-db (RustSec)](https://github.com/RustSec/advisory-db) | Database | Intermediate | Free | Git repository of all RustSec advisories — audit your dependency tree against this source. | 🟡 🆓 📦 ✅ |',
        '| [cargo-audit docs](https://github.com/RustSec/rustsec/tree/main/cargo-audit) | Docs | Intermediate | Free | Installation and CI integration for cargo-audit — automate advisory scanning on every PR. | 🟡 🆓 📦 ✅ |',
        '| [cargo-deny book](https://embarkstudios.github.io/cargo-deny/) | Guide | Intermediate | Free | Full configuration reference for licenses, bans, and sources — enterprise supply-chain policy. | 🟡 🆓 🌐 |',
        '| [cargo-vet book](https://mozilla.github.io/cargo-vet/) | Guide | Advanced | Free | Organizational audit workflow documentation — vet third-party crates with recorded reviews. | 🔴 🆓 🌐 ✅ |',
        '| [cargo-geiger README](https://github.com/rust-secure-code/cargo-geiger) | Docs | Intermediate | Free | Count unsafe functions per dependency — quantify unsafe surface area in your tree. | 🟡 🆓 📦 |',
        '| [rustls docs](https://docs.rs/rustls/latest/rustls/) | Docs | Intermediate | Free | Pure-Rust TLS configuration — prefer over OpenSSL bindings for fewer native dependencies. | 🟡 🆓 🌐 ⭐ |',
        '| [webpki-roots](https://docs.rs/webpki-roots/) | Library | Intermediate | Open Source | Mozilla CA root certificates for rustls — TLS without system certificate store dependencies. | 🟡 📦 |',
        '| [ring crypto](https://docs.rs/ring/) | Library | Advanced | Open Source | Cryptographic primitives via BoringSSL — battle-tested crypto for TLS and signing operations. | 🔴 📦 |',
        '| [argon2 crate](https://docs.rs/argon2/) | Library | Intermediate | Open Source | Password hashing per PHC winner — correct memory-hard hashing without rolling your own. | 🟡 📦 ✅ |',
        '| [bcrypt crate](https://docs.rs/bcrypt/) | Library | Intermediate | Open Source | bcrypt password hashing — legacy compatibility when migrating existing password databases. | 🟡 📦 |',
        '| [subtle crate](https://docs.rs/subtle/) | Library | Advanced | Open Source | Constant-time comparisons — prevent timing attacks when comparing secrets and MACs. | 🔴 📦 🔐 |',
        '| [constant_time_eq](https://docs.rs/constant_time_eq/) | Library | Intermediate | Open Source | Constant-time byte array comparison — lightweight alternative for MAC verification. | 🟡 📦 🔐 |',
        '| [sodiumoxide](https://docs.rs/sodiumoxide/) | Library | Advanced | Open Source | libsodium bindings for Rust — audited primitives for encryption, signing, and hashing. | 🔴 📦 |',
        '| [orion crypto](https://docs.rs/orion/) | Library | Advanced | Open Source | Pure-Rust crypto library — modern AEAD and KDF without C dependencies. | 🔴 📦 |',
        '| [cargo-fuzz book](https://rust-fuzz.github.io/book/cargo-fuzz.html) | Guide | Advanced | Free | cargo-fuzz setup and target authoring — find panics in parsers before attackers do. | 🔴 🆓 📘 |',
        '| [libfuzzer-sys](https://docs.rs/libfuzzer-sys/) | Library | Advanced | Open Source | libFuzzer bindings for Rust — in-process fuzzing integrated with cargo-fuzz workflow. | 🔴 📦 🛠 |',
        '| [afl.rs](https://github.com/rust-fuzz/afl.rs) | Tool | Advanced | Open Source | American Fuzzy Lop bindings — coverage-guided fuzzing alternative to libFuzzer. | 🔴 📦 🛠 |',
        '| [Kani docs](https://model-checking.github.io/kani/) | Docs | Advanced | Free | Model-checking Rust with bounded verification — prove absence of panics on critical paths. | 🔴 🆓 📘 |',
        '| [Prusti verifier](https://viperproject.github.io/prusti-dev/) | Tool | Advanced | Open Source | Deductive verifier for Rust — formal contracts on unsafe-free code slices. | 🔴 📦 📘 |',
        '| [cargo-auditable docs](https://github.com/rust-secure-code/cargo-auditable) | Docs | Intermediate | Free | Embed SBOM in release binaries — incident response and compliance auditing. | 🟡 🆓 📦 |',
        '| [cargo-crev book](https://github.com/crev-dev/cargo-crev/blob/master/cargo-crev/README.md) | Guide | Intermediate | Free | Cryptographic code review workflow — decentralized trust for third-party dependencies. | 🟡 🆓 📦 |',
        '| [ANSSI Rust guide (English)](https://anssi-fr.github.io/rust-guide/) | Guide | Intermediate | Free | French government secure Rust coding rules — practical checklist for hardened codebases. | 🟡 🆓 📘 ⭐ |',
        '| [Ferrous Systems Ferrocene](https://ferrous-systems.com/ferrocene/) | Product | Advanced | Paid | Qualified Rust toolchain for safety-critical industries — reference for automotive and medical paths. | 🔴 💰 📘 |',
    ],
    "Cheat Sheets": [
        '| [Rust Language Cheat Sheet (PDF)](https://cheats.rs/#formats) | Cheat sheet | Intermediate | Free | Printable PDF and PNG formats of cheats.rs — desk reference when browser tabs are full. | 🟡 🆓 ⭐ |',
        '| [Rust std library cheat sheet (PDF)](https://github.com/brson/rust-std-cheat-sheet) | Cheat sheet | Intermediate | Free | Printable std quick reference — method names and type conversions at a glance. | 🟡 🆓 📦 |',
        '| [Rust HTTP status codes (http crate)](https://docs.rs/http/latest/http/struct.StatusCode.html) | Reference | Intermediate | Free | StatusCode constants and constructors — shared across Axum, reqwest, and hyper stacks. | 🟡 🆓 🌐 |',
        '| [Rust match guards syntax](https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#match-guards) | Reference | Intermediate | Free | Conditional match arms with if guards — avoid nested match for simple predicates. | 🟡 🆓 🌐 |',
        '| [Rust turbofish syntax](https://doc.rust-lang.org/book/ch10-02-traits.html#specifying-placeholder-types-in-trait-methods-with-the-turbofish) | Reference | Intermediate | Free | Explicit type annotation with ::<> — resolve ambiguous collect() and parse() calls. | 🟡 🆓 🌐 |',
        '| [Rust deref coercion](https://doc.rust-lang.org/book/ch15-02-deref.html) | Reference | Intermediate | Free | Automatic dereferencing rules — understand why &String coerces to &str in function calls. | 🟡 🆓 🌐 📘 |',
        '| [Rust orphan rule summary](https://doc.rust-lang.org/book/ch10-02-traits.html#implementing-a-trait-on-a-type) | Reference | Intermediate | Free | Why you cannot impl external traits on external types — explains newtype wrapper patterns. | 🟡 🆓 🌐 📘 |',
        '| [Rust module tree cheat sheet](https://doc.rust-lang.org/cargo/reference/cargo-targets.html) | Reference | Intermediate | Free | Binary, lib, and test target layout — resolve mod path confusion in growing projects. | 🟡 🆓 🌐 |',
        '| [Rust semver cheat sheet](https://doc.rust-lang.org/cargo/reference/semver.html) | Reference | Intermediate | Free | What counts as breaking changes — avoid accidental major bumps when publishing libraries. | 🟡 🆓 🌐 ✅ |',
        '| [Rust Pin cheat sheet (fasterthanli)](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) | Article | Intermediate | Free | Pin explained in context of async — read when Pin projections confuse in Tokio code. | 🟡 🆓 📘 |',
        '| [Rust atomics ordering chart](https://marabos.nl/atomics/memory-orderings.html) | Reference | Advanced | Free | Visual memory ordering reference — print when writing concurrent hot paths. | 🔴 🆓 📘 |',
        '| [Rust regex quick reference](https://docs.rs/regex/latest/regex/#syntax) | Reference | Intermediate | Free | Pattern syntax summary in regex crate docs — faster than trial-and-error capture groups. | 🟡 🆓 🌐 |',
        '| [Serde field attributes](https://serde.rs/field-attrs.html) | Reference | Intermediate | Free | rename, skip, default, and flatten attributes — stop guessing derive serialization options. | 🟡 🆓 🌐 |',
        '| [Clap derive reference](https://docs.rs/clap/latest/clap/_derive/index.html) | Reference | Intermediate | Free | Arg, subcommand, and flatten attributes — CLI parsing without manual match on env vars. | 🟡 🆓 🌐 |',
        '| [Tokio spawn cheat sheet](https://tokio.rs/tokio/topics/spawning) | Reference | Intermediate | Free | spawn, spawn_blocking, and JoinHandle patterns — pick the right task type for CPU vs I/O work. | 🟡 🆓 🌐 |',
        '| [Rust cargo features matrix](https://doc.rust-lang.org/cargo/reference/features-examples.html) | Reference | Intermediate | Free | Feature flag examples from Cargo reference — optional deps without feature leakage. | 🟡 🆓 🌐 |',
        '| [Rust reference keywords table](https://doc.rust-lang.org/reference/keywords.html) | Reference | Beginner | Free | Raw identifier syntax with r# prefix — use reserved words as field names when needed. | 🟢 🆓 🌐 |',
        '| [Rust primitive casts table](https://doc.rust-lang.org/reference/expressions/operator-expr.html#r-cast.as) | Reference | Intermediate | Free | as casts vs TryFrom — avoid silent truncation in numeric conversions. | 🟡 🆓 🌐 |',
        '| [Rust trait object sizing](https://doc.rust-lang.org/reference/types/trait-object.html) | Reference | Advanced | Free | Wide pointer layout for dyn Trait — understand fat pointer costs vs impl Trait. | 🔴 🆓 🌐 📘 |',
        '| [Rust cfg attribute list](https://doc.rust-lang.org/reference/conditional-compilation.html#set-configuration-options) | Reference | Intermediate | Free | target_os, target_arch, and feature cfg values — platform-specific compilation without runtime checks. | 🟡 🆓 🌐 |',
    ],
    "Interview Prep": [
        '| [Rust interview handbook (GitHub)](https://github.com/yoshuawuyts/rust-interview-handbook) | Guide | Intermediate | Free | Curated ownership and concurrency questions — rehearse aloud before phone screens. | 🟡 🆓 📘 |',
        '| [Rust quiz (dtolnay)](https://dtolnay.github.io/rust-quiz/) | Quiz | Advanced | Free | Subtle language semantics puzzles — exposes gaps before staff-level technical interviews. | 🔴 🆓 🛠 🔥 |',
        '| [Rustlings interview mode](https://github.com/rust-lang/rustlings) | Exercises | Beginner | Free | Re-run exercises under time pressure — simulates whiteboard speed for syntax fluency. | 🟢 🆓 🛠 |',
        '| [Rust standard library source reading](https://doc.rust-lang.org/src/std/lib.rs.html) | Codebase | Advanced | Free | Read Vec and HashMap implementations — systems interviews ask how standard collections work. | 🔴 🆓 🌐 📘 |',
        '| [Rust HashMap internals (hashbrown)](https://github.com/rust-lang/hashbrown) | Codebase | Advanced | Free | Swiss table implementation study — performance and probing strategy interview topics. | 🔴 🆓 📦 📘 |',
        '| [Rust concurrency interview topics](https://doc.rust-lang.org/book/ch16-00-concurrency.html) | Reference | Intermediate | Free | Threads, channels, and Mutex patterns — rehearse trade-offs between message passing and shared state. | 🟡 🆓 🌐 |',
        '| [Rust async interview topics (Gjengset)](https://www.youtube.com/watch?v=5_1C_k33WBw) | Video | Advanced | Free | State machines and Pin in async Rust — common senior-level live coding discussion topic. | 🔴 🆓 📘 |',
        '| [Rust iterator interview patterns](https://doc.rust-lang.org/std/iter/trait.Iterator.html) | Reference | Intermediate | Free | Iterator trait methods — whiteboard filter/map/fold problems expect fluent iterator chains. | 🟡 🆓 🌐 🛠 |',
        '| [Rust smart pointer comparison](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html) | Reference | Intermediate | Free | Box vs Rc vs Arc vs RefCell — interviewers test when each allocation strategy applies. | 🟡 🆓 🌐 📘 |',
        '| [Rust error handling interview guide](https://nick.groenen.me/posts/rust-error-handling/) | Article | Intermediate | Free | Result vs panic vs anyhow — articulate error strategy per application layer in interviews. | 🟡 🆓 📘 |',
        '| [Rust lifetime elision rules](https://doc.rust-lang.org/reference/lifetime-elision.html) | Reference | Advanced | Free | When annotations are inferred — explain elision rules confidently in language fundamentals rounds. | 🔴 🆓 🌐 📘 |',
        '| [Rust Send Sync explainer](https://doc.rust-lang.org/nomicon/send-and-sync.html) | Reference | Advanced | Free | Nomicon chapter on thread safety markers — almost always asked in Rust systems interviews. | 🔴 🆓 🌐 📘 ⭐ |',
        '| [Rust trait object vs generics](https://doc.rust-lang.org/book/ch17-02-trait-objects.html) | Reference | Intermediate | Free | Static vs dynamic dispatch trade-offs — articulate performance and API design implications. | 🟡 🆓 🌐 📘 |',
        '| [Rust string types interview guide](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) | Article | Beginner | Free | &str, String, Cow, and OsStr — first-week question that still appears in mid-level screens. | 🟢 🆓 📘 |',
        '| [fd codebase architecture](https://github.com/sharkdp/fd) | Codebase | Intermediate | Free | Study a medium-sized Rust CLI — module layout and error handling patterns for portfolio discussions. | 🟡 🆓 📦 🚀 |',
        '| [bat codebase architecture](https://github.com/sharkdp/bat) | Codebase | Intermediate | Free | Larger CLI with syntect integration — discuss testing and feature flags in architecture interviews. | 🟡 🆓 📦 |',
        '| [Rust linked list (too-many-lists)](https://rust-unofficial.github.io/too-many-lists/) | Book (online) | Advanced | Free | Ownership edge cases through linked lists — memorable examples for borrow-checker discussion rounds. | 🔴 🆓 📘 🛠 |',
        '| [Rust atomics interview prep](https://marabos.nl/atomics/) | Book (online) | Advanced | Free | Memory ordering questions for concurrent systems roles — read before infra team interviews. | 🔴 🆓 📘 |',
        '| [Rust Brain Teasers book](https://pragprog.com/titles/hwrustbrain/) | Book | Advanced | Paid | Subtle language puzzles — interview prep disguised as entertainment for senior candidates. | 🔴 💰 📘 🛠 |',
        '| [Rust RFC 2052 (impl trait)](https://rust-lang.github.io/rfcs/1522-conservative-impl-trait.html) | Reference | Advanced | Free | impl Trait in return position — staff interviews may probe opaque return type semantics. | 🔴 🆓 📘 |',
    ],
    "Awesome Lists": [
        '| [awesome-rust-gh-pages](https://github.com/rust-unofficial/awesome-rust/tree/master/docs) | Awesome list | Intermediate | Free | Rendered site mirror of rust-unofficial/awesome-rust — browse categories without GitHub markdown. | 🟡 🆓 |',
        '| [awesome-rust-lang](https://github.com/janikvonrotz/awesome-rust) | Awesome list | Intermediate | Free | Alternative community index with different categorization — supplementary discovery source. | 🟡 🆓 |',
        '| [awesome-rust-oss](https://github.com/ctjhoa/rust-learning) | Awesome list | Beginner | Free | Learning-focused subset of community resources — tutorials and exercises beyond this curated list. | 🟢 🆓 |',
        '| [awesome-rust-web](https://github.com/robrichards/awesome-rust-web) | Awesome list | Intermediate | Free | Web framework and HTTP crate index — deeper coverage than this list\'s framework section. | 🟡 🆓 🚀 |',
        '| [awesome-rust-gamedev](https://github.com/RazrFalcon/awesome-rust-gamedev) | Awesome list | Intermediate | Free | Game development crates and engines — specialization index after Bevy fundamentals. | 🟡 🆓 🚀 |',
        '| [awesome-rust-machine-learning](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning) | Awesome list | Advanced | Free | ML and data science crates — linfa, ndarray, and tch ecosystem discovery. | 🔴 🆓 |',
        '| [awesome-rust-embedded (mirror)](https://github.com/rust-embedded/awesome-embedded-rust) | Awesome list | Advanced | Free | Duplicate canonical embedded list — HALs, BSPs, and no_std crates for microcontroller work. | 🔴 🆓 |',
        '| [awesome-cli-rust](https://github.com/sts10/rust-command-line-utilities) | Awesome list | Intermediate | Free | Curated list of Rust CLI tools — inspiration for portfolio CLI projects and code reading. | 🟡 🆓 🛠 |',
        '| [awesome-rust-telegram](https://github.com/ozkriff/awesome-rust-gamedev) | Awesome list | Intermediate | Free | Community-maintained discovery channels — find new lists as the ecosystem grows. | 🟡 🆓 |',
        '| [awesome-blockchain-rust](https://github.com/rust-in-blockchain/awesome-blockchain-rust) | Awesome list | Advanced | Free | Blockchain and cryptography projects in Rust — niche career path resource index. | 🔴 🆓 |',
        '| [awesome-rust-cloud](https://github.com/cloud-native/awesome-cloud-native) | Awesome list | Advanced | Free | Cloud-native Rust projects — Kubernetes operators and observability tooling discovery. | 🔴 🆓 |',
        '| [awesome-rust-ffi](https://github.com/alexcrichton/awesome-rust-ffi) | Awesome list | Advanced | Free | FFI bindings and interop tools — C, C++, and Python integration resource index. | 🔴 🆓 📘 |',
    ],
    "Communities": [
        '| [Rust Zulip (official)](https://rust-lang.zulipchat.com/) | Chat | Intermediate | Free | Official Zulip for Rust teams and working groups — structured threads for async, embedded, and compiler topics. | 🟡 🆓 🌐 |',
        '| [This Week in Rust submissions](https://github.com/rust-lang/this-week-in-rust) | Newsletter | Intermediate | Free | Contribute links and project announcements — visibility for your open-source Rust work. | 🟡 🆓 📦 |',
        '| [Rust Magazine](https://rustmagazine.org/) | Magazine | Intermediate | Free | Community-written articles on Rust projects and techniques — long-form stories beyond blog posts. | 🟡 🆓 📘 |',
        '| [Rustacean Station podcast](https://rustacean-station.org/) | Podcast | Intermediate | Free | Interviews with Rust maintainers and authors — commute-friendly ecosystem context. | 🟡 🆓 🔥 |',
        '| [New Rustacean podcast (archive)](https://www.newrustacean.com/) | Podcast | Beginner | Free | Classic beginner podcast archive — foundational episodes still relevant for ownership concepts. | 🟢 🆓 📘 |',
        '| [Rust Linz meetup](https://www.meetup.com/Rust-Linz/) | Meetup | Intermediate | Free | Austrian Rust community events — model for finding regional meetups worldwide. | 🟡 🆓 |',
        '| [Rust London meetup](https://www.meetup.com/rust-london/) | Meetup | Intermediate | Free | Large European Rust meetup — recorded talks on production adoption and library design. | 🟡 🆓 🔥 |',
        '| [Rust NYC meetup](https://www.meetup.com/rust-nyc/) | Meetup | Intermediate | Free | US East Coast Rust community — networking for Rust job seekers in New York. | 🟡 🆓 |',
        '| [Rust Berlin meetup](https://www.meetup.com/rust-ber/) | Meetup | Intermediate | Free | German Rust community hub — talks from European companies shipping Rust in production. | 🟡 🆓 |',
        '| [Rust Tokyo](https://rust.tokyo/) | Conference | Intermediate | Paid | Japan Rust conference — Asian Rust community and recorded talks on web and systems topics. | 🟡 💰 📘 |',
        '| [RustChinaConf](https://rustcc.cn/) | Conference | Intermediate | Free | Chinese Rust community conference — growing regional ecosystem beyond English-language resources. | 🟡 🆓 |',
        '| [RustFest (archive)](https://rustfest.org/) | Conference | Intermediate | Free | Historical Rust conference recordings — foundational talks on language design and adoption. | 🟡 🆓 📘 |',
        '| [Rustacean IRC (Libera)](https://web.libera.chat/#rust) | Chat | Beginner | Free | Long-running IRC channel for real-time help — still active for quick syntax questions. | 🟢 🆓 |',
        '| [Rust Beginners IRC](https://web.libera.chat/#rust-beginners) | Chat | Beginner | Free | Dedicated IRC channel for newcomers — lower barrier than general Rust channels. | 🟢 🆓 |',
        '| [Rust Embedded Matrix (official)](https://matrix.to/#/#rust-embedded:matrix.org) | Chat | Advanced | Free | no_std and microcontroller help — specialized when users.rust-lang.org embedded tags are quiet. | 🔴 🆓 |',
        '| [Rust Gamedev Discord](https://discord.gg/yNtPTb2) | Chat | Intermediate | Free | Bevy and graphics real-time help — active for ECS and rendering questions. | 🟡 🆓 🚀 |',
        '| [Rust OSDev Discord](https://discord.gg/EVhFMnAs) | Chat | Advanced | Free | Operating system development in Rust — kernel, bootloader, and no_std community. | 🔴 🆓 |',
        '| [Rust WASM Matrix](https://matrix.to/#/#rust-wasm:matrix.org) | Chat | Intermediate | Free | WebAssembly-specific Rust help — wasm-bindgen and browser deployment questions. | 🟡 🆓 🚀 |',
        '| [Rust Foundation newsletter](https://foundation.rust-lang.org/news/) | Newsletter | Intermediate | Free | Foundation announcements and member spotlights — enterprise adoption signal and job market context. | 🟡 🆓 🌐 |',
        '| [Rust Project newsletter](https://www.rust-lang.org/announcements) | Newsletter | Intermediate | Free | Official project announcements — release dates, events, and governance updates. | 🟡 🆓 🌐 |',
    ],
    "Books": [
        '| [The Rust Programming Language (3rd ed. preview)](https://doc.rust-lang.org/book/) | Book (online) | Beginner | Free | Latest Book edition as it evolves — track new chapters before print editions catch up. | 🟢 🆓 🌐 |',
        '| [Rust in Action (Manning)](https://www.manning.com/books/rust-in-action) | Book | Intermediate | Paid | Systems programming through hands-on projects — ideal for developers who learn by building. | 🟡 💰 🛠 🚀 |',
        '| [Command-Line Rust (No Starch)](https://nostarch.com/command-line-rust) | Book | Intermediate | Paid | Build CLI tools chapter by chapter — practical companion to Clap and std I/O mastery. | 🟡 💰 🛠 🚀 |',
        '| [Rust for Network Programming (Packt)](https://www.packtpub.com/product/rust-for-network-programming/9781803233726) | Book | Intermediate | Paid | TCP, UDP, and HTTP from scratch — network fundamentals before framework abstractions. | 🟡 💰 📘 |',
        '| [Mastering Rust (Packt)](https://www.packtpub.com/product/mastering-rust-second-edition/9781835889009) | Book | Advanced | Paid | Advanced patterns including unsafe, macros, and FFI — breadth after a year of daily Rust. | 🔴 💰 📘 |',
        '| [Rust Web Development (Manning)](https://www.manning.com/books/rust-web-development) | Book | Intermediate | Paid | Full-stack web with Actix and Diesel — alternative to Zero To Production\'s Axum stack. | 🟡 💰 🚀 |',
        '| [Rust Projects (Packt)](https://www.packtpub.com/product/rust-projects/9781789535632) | Book | Intermediate | Paid | Varied project chapters from CLI to web — breadth when one tutorial stack feels narrow. | 🟡 💰 🚀 |',
        '| [Beginning Rust 2021 (Apress)](https://www.apress.com/gp/book/9781484271795) | Book | Beginner | Paid | Updated beginner edition with async coverage — gentle exercises for first-time Rust learners. | 🟢 💰 🛠 |',
        '| [Learn Rust with Examples (Apress)](https://www.apress.com/gp/book/9781484285549) | Book | Beginner | Paid | Example-driven learning supplementing the Book — more drills for syntax reinforcement. | 🟢 💰 🛠 |',
        '| [Rust Cookbook (community fork)](https://github.com/rust-lang-nursery/rust-cookbook) | Book (online) | Beginner | Free | Community-maintained recipe collection — task-oriented snippets for common problems. | 🟢 🆓 📦 🛠 |',
        '| [The Little Book of Rust Macros](https://danielkeep.github.io/tlborm/book/) | Book (online) | Advanced | Free | macro_rules! deep dive — demystify declarative macros when derives are not enough. | 🔴 🆓 📘 |',
        '| [Rust API Guidelines (print mindset)](https://rust-lang.github.io/api-guidelines/) | Guide | Intermediate | Free | Treat as a book-length style guide — read cover to cover before publishing libraries. | 🟡 🆓 🌐 📘 |',
        '| [Zero To Production (companion repo)](https://github.com/LukeMathWalker/zero-to-production) | Book | Intermediate | Free | Open-source code accompanying the paid book — study architecture without purchasing first. | 🟡 🆓 📦 🚀 |',
        '| [Rust in 30 minutes (Microsoft)](https://learn.microsoft.com/en-us/training/modules/rust-introduction/) | Book | Beginner | Free | Quick Microsoft module — orientation before committing to the full Book. | 🟢 🆓 🛠 |',
        '| [Rust By Example (print companion)](https://doc.rust-lang.org/rust-by-example/) | Book (online) | Beginner | Free | Runnable examples for every feature — keep open alongside the Book for code-first learners. | 🟢 🆓 🌐 🛠 |',
        '| [Rust for the IoT (Packt)](https://www.packtpub.com/product/rust-for-the-iot/9781805125494) | Book | Advanced | Paid | Embedded and IoT patterns — firmware and sensor projects for hardware-oriented developers. | 🔴 💰 🛠 |',
        '| [Creative Projects for Rust (No Starch)](https://nostarch.com/creative-projects-rust) | Book | Intermediate | Paid | Visual and creative coding projects — engaging path for learners who find CLI tools dry. | 🟡 💰 🚀 |',
        '| [Rust Servers, Services, and Apps (Manning)](https://www.manning.com/books/rust-servers-services-and-apps) | Book | Intermediate | Paid | Backend service patterns — complements Zero To Production with alternative project structures. | 🟡 💰 🚀 |',
        '| [Rust in Practice (Manning)](https://www.manning.com/books/rust-in-practice) | Book | Intermediate | Paid | Real-world patterns for production codebases — error handling, testing, and module design. | 🟡 💰 📘 |',
        '| [Rust for Rustaceans (companion errata)](https://rust-for-rustaceans.com/) | Book | Advanced | Free | Errata and updates for the No Starch advanced title — keep current after purchase. | 🔴 🆓 📘 |',
    ],
    "Courses": [
        '| [Rust Book official course path](https://www.rust-lang.org/learn) | Course | Beginner | Free | Official learning path linking Book, Rustlings, and community resources — zero-cost structured entry. | 🟢 🆓 🌐 ⭐ |',
        '| [100 Exercises course (Mainmatter)](https://github.com/mainmatter/100-exercises-to-learn-rust) | Course | Beginner | Free | Progressive workshop curriculum — corporate training structure available free on GitHub. | 🟢 🆓 📦 🛠 ⭐ |',
        '| [Rustlings official workshop](https://github.com/rust-lang/rustlings#runnable-exercises) | Course | Beginner | Free | Self-paced pairing of Book chapters with exercises — built-in progression without paywall. | 🟢 🆓 🛠 |',
        '| [Zero To Production course (paid)](https://www.zero2prod.com/) | Course | Intermediate | Paid | Production web service course with tests and deploy — bridges tutorials to shipping habits. | 🟡 💰 🚀 ⭐ |',
        '| [Rust Adventure courses](https://rustadventure.dev/) | Course | Intermediate | Paid | Project-based paid paths for web, games, and tooling — structured when YouTube feels scattered. | 🟡 💰 🚀 |',
        '| [Ferrous Systems training catalog](https://ferrous-systems.com/training/) | Course | Intermediate | Paid | Commercial courses from embedded and async experts — employer-sponsored upskilling option. | 🟡 💰 🛠 |',
        '| [Udacity Rust course](https://www.udacity.com/course/rust-programming--ud301) | Course | Intermediate | Paid | Nanodegree-style Rust modules — structured video and project assignments. | 🟡 💰 🛠 |',
        '| [Pluralsight Rust path](https://www.pluralsight.com/paths/rust) | Course | Intermediate | Paid | Video course path for enterprise learners — integrates with corporate training platforms. | 🟡 💰 |',
        '| [LinkedIn Learning Rust](https://www.linkedin.com/learning/topics/rust) | Course | Beginner | Paid | Short video modules for professionals — low-friction introduction during lunch breaks. | 🟢 💰 |',
        '| [Codecademy Learn Rust](https://www.codecademy.com/learn/learn-rust) | Course | Beginner | Freemium | Interactive browser exercises — syntax practice before local toolchain setup. | 🟢 🆓 💰 🛠 |',
        '| [Exercism Rust syllabus](https://exercism.org/tracks/rust) | Course | Beginner | Free | Concept exercises with optional mentoring — reinforces Book chapters through repetition. | 🟢 🆓 🛠 |',
        '| [Rust by Practice course](https://practice.rs/) | Course | Beginner | Free | Topic-indexed drills from syntax through modules — companion after Rustlings set one. | 🟢 🆓 🛠 🔥 |',
        '| [Microsoft Rust learning path](https://learn.microsoft.com/en-us/training/paths/rust-first-steps/) | Course | Beginner | Free | Official Microsoft modules with sandbox — low friction for Windows-centric developers. | 🟢 🆓 🛠 |',
        '| [Low Level Academy (Rust)](https://lowlevel.academy/) | Course | Advanced | Paid | Low-level systems topics including Rust — kernel and hardware-oriented video courses. | 🔴 💰 📘 |',
        '| [Tim McNamara Rust course (YouTube)](https://www.youtube.com/watch?v=MsocPEZBd-M) | Video | Beginner | Free | Long-form community Rust course — weekend binge alongside Rustlings. | 🟢 🆓 |',
        '| [Ryan Levick Rust videos](https://www.youtube.com/c/RyanLevicksVideos) | Video | Beginner | Free | Microsoft Rust advocate tutorials — Windows and Azure integration context for learners. | 🟢 🆓 |',
    ],
    "Career": [
        '| [Rust jobs on LinkedIn](https://www.linkedin.com/jobs/search/?keywords=rust%20developer) | Job board | Intermediate | Free | Broad job search for Rust roles — supplement niche boards with mainstream listings. | 🟡 🆓 |',
        '| [Indeed Rust developer jobs](https://www.indeed.com/q-rust-developer-jobs.html) | Job board | Intermediate | Free | General job aggregator Rust filter — volume beyond specialized Rust-only boards. | 🟡 🆓 |',
        '| [RemoteOK Rust filter](https://remoteok.com/remote-rust-jobs) | Job board | Intermediate | Free | Remote-first Rust positions — useful for distributed team job seekers. | 🟡 🆓 🔥 |',
        '| [We Work Remotely Rust](https://weworkremotely.com/remote-jobs/search?term=rust) | Job board | Intermediate | Free | Remote job board with Rust filter — curated remote-first company listings. | 🟡 🆓 |',
        '| [AngelList Rust startups](https://wellfound.com/role/l/rust-developer) | Job board | Intermediate | Free | Startup-focused Rust roles — early-stage companies adopting Rust for infrastructure. | 🟡 🆓 |',
        '| [Ferrous Systems careers page](https://ferrous-systems.com/careers/) | Job board | Advanced | Free | Rust consultancy hiring — embedded and safety-critical career path model. | 🔴 🆓 🚀 |',
        '| [Mainmatter careers](https://mainmatter.com/careers/) | Job board | Advanced | Free | Leading Rust consultancy openings — consulting and training career paths. | 🔴 🆓 🚀 |',
        '| [1Password engineering blog](https://1password.com/blog/) | Blog | Intermediate | Free | Product company Rust adoption stories — read job descriptions for skill expectations. | 🟡 🆓 |',
        '| [Figma Rust blog posts](https://www.figma.com/blog/) | Blog | Intermediate | Free | Design tool company using Rust — evidence of Rust beyond infra and crypto stereotypes. | 🟡 🆓 |',
        '| [Dropbox Nucleus (Rust)](https://dropbox.tech/application/why-we-built-nucleus-a-rust-based-platform-for-low-latency-apps) | Blog | Advanced | Free | Dropbox low-latency platform in Rust — case study for backend infrastructure interviews. | 🔴 🆓 📘 |',
        '| [AWS Firecracker blog](https://firecracker-microvm.github.io/) | Blog | Advanced | Free | Rust microVM technology at AWS — virtualization and cloud infrastructure career context. | 🔴 🆓 📘 |',
        '| [Meta Rust adoption](https://engineering.fb.com/) | Blog | Intermediate | Free | Meta engineering blog Rust posts — large-scale production adoption talking points. | 🟡 🆓 |',
        '| [Google Rust in Android](https://security.googleblog.com/) | Blog | Advanced | Free | Android Rust adoption for memory safety — mobile and systems career path evidence. | 🔴 🆓 📘 |',
        '| [Microsoft Rust adoption](https://devblogs.microsoft.com/) | Blog | Intermediate | Free | Microsoft Rust projects including Windows and Azure — enterprise adoption stories. | 🟡 🆓 🌐 |',
        '| [Rust Foundation jobs board](https://foundation.rust-lang.org/) | Directory | Intermediate | Free | Foundation member companies — research employers investing in Rust open source. | 🟡 🆓 🌐 |',
    ],
}

NEW_FAQ = [
    '| 31 | **What is the difference between `&T` and `&mut T` in APIs?** | Shared read-only access vs exclusive mutable access — design APIs to take `&T` when mutation is not needed, reducing borrow conflicts. |',
    '| 32 | **When should I use `Cow<str>`?** | When a function might borrow or own string data — avoids forcing callers to allocate when a borrow suffices. |',
    '| 33 | **How do I handle `?` in main()?** | Use `fn main() -> Result<(), Box<dyn Error>>` or `anyhow::Result<()>` — propagates errors cleanly from CLI entry points. |',
    '| 34 | **What is `#![deny(warnings)]` for?** | Crate-level attribute treating warnings as errors — enforce clean builds in libraries you publish. |',
    '| 35 | **How do I test private functions?** | Prefer testing through public API; use `#[cfg(test)] mod tests` in the same file for unit tests of internals. |',
    '| 36 | **What is a `Pin<Box<dyn Future>>`?** | Pinned heap-allocated future for async trait objects — required when async methods return opaque futures stored in collections. |',
    '| 37 | **Should library crates use `unwrap()` in examples?** | Doc examples may use `unwrap()` for brevity; library implementation code should return `Result` per [API Guidelines](#-intermediate). |',
    '| 38 | **How do I profile compile times?** | `cargo build -Z timings` on nightly or `cargo llvm-lines` — identify monomorphization bloat per [Performance](#-performance). |',
]

NEW_PITFALLS = [
    '| **Using `async fn` in main without a runtime** | `#![tokio::main]` attribute or manual runtime creation — async main needs an executor to poll futures. | Add `#[tokio::main]` or `#[async_std::main]` or build runtime explicitly | 🟡 🛠 |',
    '| **Holding locks across await points** | Deadlocks when async tasks interleave | Release locks before `.await`; restructure to avoid `MutexGuard` across suspension | 🔴 📘 |',
    '| **Ignoring `Send` in generic bounds** | Spawn failures with opaque compiler errors | Add `T: Send + \'static` bounds on types moved into `tokio::spawn` | 🟡 🛠 |',
    '| **Feature unification surprises** | Optional dep enabled in one crate affects all | Use weak dependency features; read [Cargo features](#-cheat-sheets) before workspace splits | 🟡 📘 |',
    '| **Testing only debug builds** | Release-only optimizations expose bugs | Run `cargo test --release` for performance-critical code paths before shipping | 🔴 🛠 |',
]

TARGET_SECTIONS = [
    "Official & Docs", "Beginner", "Intermediate", "Advanced",
    "Ecosystem & Tools", "Frameworks", "Testing", "Performance",
    "Security", "Cheat Sheets", "Interview Prep", "Awesome Lists",
    "Communities", "Books", "Courses", "Career",
]


def expand_section(lines: list[str], section_name: str) -> list[str]:
    """Insert new rows after existing table rows in a section."""
    new_rows = NEW_ROWS.get(section_name, [])
    if not new_rows:
        return lines

    result = []
    in_section = False
    in_table = False
    inserted = False

    for line in lines:
        if line.startswith("## ") and section_name in line:
            in_section = True
            in_table = False
            inserted = False
            result.append(line)
            continue

        if in_section and line.startswith("## "):
            in_section = False
            in_table = False

        if in_section and line.startswith("| Resource |"):
            in_table = True
            result.append(line)
            continue

        if in_section and in_table and line.startswith("| --- |"):
            result.append(line)
            continue

        if in_section and in_table and line.startswith("| [") and not inserted:
            result.append(line)
            continue

        if in_section and in_table and not line.startswith("| [") and not inserted:
            # End of table — insert new rows before this line
            for row in new_rows:
                result.append(row)
            inserted = True
            in_table = False
            result.append(line)
            continue

        result.append(line)

    return result


def insert_before_section(lines: list[str], marker: str, new_lines: list[str]) -> list[str]:
    """Insert lines before a section header containing marker."""
    result = []
    for line in lines:
        if marker in line and line.startswith("## ") and not any(
            l in result[-5:] if result else False for l in new_lines
        ):
            # Check we haven't already inserted
            pass
        if marker in line and line.startswith("## ") and new_lines[0] not in "\n".join(result[-20:]):
            result.extend(new_lines)
        result.append(line)
    return result


def main():
    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Expand each target section
    for section in TARGET_SECTIONS:
        lines = expand_section(lines, section)

    # Add FAQ entries before glossary
    faq_idx = next(i for i, l in enumerate(lines) if l.startswith("## ") and "Glossary" in l)
    # Find last FAQ row (before ---)
    insert_at = faq_idx - 1
    while insert_at > 0 and lines[insert_at].strip() != "---":
        insert_at -= 1
    # Insert before the --- separator before Glossary
    for row in reversed(NEW_FAQ):
        lines.insert(insert_at, row)

    # Add pitfalls before Contributing
    contrib_idx = next(i for i, l in enumerate(lines) if l.startswith("## ") and "Contributing" in l)
    insert_at = contrib_idx - 1
    while insert_at > 0 and lines[insert_at].strip() != "---":
        insert_at -= 1
    for row in reversed(NEW_PITFALLS):
        lines.insert(insert_at, row)

    output = "\n".join(lines) + "\n"
    README.write_text(output, encoding="utf-8")
    print(f"Written {output.count(chr(10)) + 1} lines")


if __name__ == "__main__":
    main()
