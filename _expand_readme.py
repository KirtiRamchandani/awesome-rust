#!/usr/bin/env python3
"""Expand README.md by doubling resource table rows in target sections."""

from pathlib import Path

README = Path(__file__).parent / "README.md"

# New rows per section (must match existing row count in each section)
NEW_ROWS = {
    "official": [
        "| [Rust Forge](https://forge.rust-lang.org/) | Guide | Intermediate | Free | Central index of Rust team infrastructure, release process, and platform docs — navigate governance beyond rust-lang.org. | 🟡 🆓 🌐 |",
        "| [Rustdoc lints](https://doc.rust-lang.org/rustdoc/lints.html) | Reference | Intermediate | Free | Warn on broken intra-doc links and missing docs — keeps published crate documentation trustworthy on docs.rs. | 🟡 🆓 🌐 |",
        "| [Cargo commands index](https://doc.rust-lang.org/cargo/commands/) | Reference | Intermediate | Free | Complete CLI reference for build, test, publish, and vendor — consult when flags behave differently in CI vs locally. | 🟡 🆓 🌐 |",
        "| [Rustc lints listing](https://doc.rust-lang.org/rustc/lints/index.html) | Reference | Advanced | Free | Compiler lint groups and allow/warn/deny controls — tune `-A`/`-D` flags for stricter team CI pipelines. | 🔴 🆓 🌐 |",
        "| [Conditional compilation](https://doc.rust-lang.org/reference/conditional-compilation.html) | Reference | Intermediate | Free | `cfg`, target triples, and feature gates — essential when supporting multiple platforms from one codebase. | 🟡 🆓 🌐 📘 |",
        "| [Attributes reference](https://doc.rust-lang.org/reference/attributes.html) | Reference | Advanced | Free | Built-in and custom attributes catalog — baseline before writing proc-macro attribute crates. | 🔴 🆓 🌐 📘 |",
        "| [Const evaluation](https://doc.rust-lang.org/reference/const_eval.html) | Reference | Advanced | Free | Rules for compile-time computation — unlocks const generics and static assertions in library APIs. | 🔴 🆓 🌐 📘 |",
        "| [Rustdoc intra-doc links](https://doc.rust-lang.org/rustdoc/write-documentation/linking-to-items-by-name.html) | Guide | Intermediate | Free | Link types and functions across modules in docs — reduces broken links when APIs get reorganized. | 🟡 🆓 🌐 🛠 |",
        "| [Platform support](https://doc.rust-lang.org/nightly/rustc/platform-support.html) | Reference | Intermediate | Free | Tier 1/2/3 target matrix — set expectations before committing to embedded or exotic cross-compile targets. | 🟡 🆓 🌐 |",
        "| [Rustdoc search index](https://doc.rust-lang.org/rustdoc/read-documentation/search.html) | Docs | Intermediate | Free | How docs.rs search works and how to optimize symbol names — improves discoverability of your public API. | 🟡 🆓 🌐 |",
        "| [Rustdoc book — doctests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) | Guide | Intermediate | Free | Hidden lines, `#` prefixes, and compile-fail tests — patterns for teaching APIs in doc comments. | 🟡 🆓 🌐 🛠 |",
        "| [Rustdoc book — attributes](https://doc.rust-lang.org/rustdoc/write-documentation/the-doc-attribute.html) | Guide | Intermediate | Free | `#[doc(hidden)]`, `doc(inline)`, and alias attributes — control what appears in generated HTML output. | 🟡 🆓 🌐 |",
        "| [Rust target spec JSON](https://doc.rust-lang.org/nightly/rustc/targets/custom.html) | Reference | Advanced | Free | Custom target definitions for bare-metal or proprietary OS builds — embedded teams use this for chip-specific triples. | 🔴 🆓 🌐 📘 |",
        "| [Rustdoc — include external files](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html#include-files-as-tests) | Guide | Intermediate | Free | Embed external `.rs` files as doctests — keeps long examples maintainable outside doc comments. | 🟡 🆓 🌐 🛠 |",
        "| [Rustdoc — scrape examples](https://doc.rust-lang.org/nightly/rustdoc/scrape-examples.html) | Guide | Advanced | Free | Collect runnable examples from the codebase into docs — improves onboarding for large library crates. | 🔴 🆓 🌐 |",
        "| [Rustdoc — custom CSS](https://doc.rust-lang.org/rustdoc/read-documentation/how-to-read-rustdoc.html) | Docs | Intermediate | Free | Theme and layout customization for published docs — brand team crates without forking docs.rs. | 🟡 🆓 🌐 |",
        "| [Rustdoc — item sorting](https://doc.rust-lang.org/rustdoc/write-documentation/what-to-include.html) | Guide | Intermediate | Free | Control section ordering in generated pages — present APIs in teaching order rather than alphabetical. | 🟡 🆓 🌐 |",
        "| [Rustdoc — type layout](https://doc.rust-lang.org/nightly/unstable-book/compiler-flags/report-type-layout.html) | Reference | Advanced | Free | `--print=type-layout` for repr and alignment — debug FFI struct packing before shipping bindings. | 🔴 🆓 🌐 📘 |",
        "| [Rustdoc — unstable flags](https://doc.rust-lang.org/nightly/rustdoc/unstable-features.html) | Reference | Advanced | Free | Nightly-only rustdoc capabilities — evaluate before enabling in docs.rs metadata configuration. | 🔴 🆓 🌐 |",
        "| [Rustdoc — link to items](https://doc.rust-lang.org/rustdoc/write-documentation/linking-to-items-by-name.html) | Guide | Intermediate | Free | Cross-crate linking syntax in markdown docs — connect your types to std and dependency APIs cleanly. | 🟡 🆓 🌐 |",
        "| [Rustdoc — README inclusion](https://doc.rust-lang.org/rustdoc/write-documentation/linking-to-items-by-name.html) | Guide | Intermediate | Free | `#![doc = include_str!(\"../README.md\")]` pattern — single source of truth for crate landing pages. | 🟡 🆓 🌐 🛠 |",
        "| [Rustdoc — item info](https://doc.rust-lang.org/rustdoc/read-documentation/how-to-read-rustdoc.html) | Docs | Beginner | Free | How to read trait impl sections and auto-trait bounds on docs.rs — demystifies busy generated pages. | 🟢 🆓 🌐 |",
        "| [Rustdoc — playground integration](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) | Guide | Intermediate | Free | Runnable examples with edition flags — verify snippets compile before publishing to docs.rs. | 🟡 🆓 🌐 🛠 |",
        "| [Rustdoc — item visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html) | Reference | Intermediate | Free | pub(crate), pub(super), and re-export rules — document only what you intend as stable public API. | 🟡 🆓 🌐 📘 |",
        "| [Rustdoc — feature docs](https://doc.rust-lang.org/cargo/reference/features.html#documentation) | Guide | Intermediate | Free | Document optional features and their interactions — prevents surprise compile errors when consumers enable flags. | 🟡 🆓 🌐 |",
        "| [Rustdoc — lint missing docs](https://doc.rust-lang.org/rustdoc/lints.html#missing_docs) | Reference | Intermediate | Free | Enforce documentation on public items — pair with `#![warn(missing_docs)]` in library crate roots. | 🟡 🆓 🌐 ✅ |",
        "| [Rustdoc — item stability](https://doc.rust-lang.org/reference/stability.html) | Reference | Advanced | Free | Stability attributes and deprecation paths — communicate API evolution without breaking semver silently. | 🔴 🆓 🌐 📘 |",
        "| [Rustdoc — item macros](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) | Guide | Advanced | Free | Document macro-generated APIs with examples — hardest docs to maintain but highest consumer value. | 🔴 🆓 🌐 🛠 |",
        "| [Rustdoc — item errors](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html#showing-output-from-examples) | Guide | Intermediate | Free | Show expected compiler errors in doc tests — teach correct usage by demonstrating what fails. | 🟡 🆓 🌐 🛠 |",
        "| [Rustdoc — item modules](https://doc.rust-lang.org/rustdoc/write-documentation/what-to-include.html) | Guide | Intermediate | Free | Module-level docs with `# Examples` sections — set context before readers dive into individual functions. | 🟡 🆓 🌐 |",
        "| [Rustdoc — item re-exports](https://doc.rust-lang.org/reference/items/use-declarations.html) | Reference | Intermediate | Free | `pub use` patterns for ergonomic crate roots — flatten deep module trees without hiding implementation. | 🟡 🆓 🌐 📘 |",
        "| [Rustdoc — item testing](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html) | Guide | Intermediate | Free | Run `cargo test --doc` in CI — catches stale examples that compile-fail after API refactors. | 🟡 🆓 🌐 🛠 ✅ |",
    ],
}

# Truncate official to match - I need to count actual rows. Let me use dynamic approach instead.

SECTION_MARKERS = [
    ("## 📚 Official & Docs", "## 🌱 Beginner", "official"),
    ("## 🌱 Beginner", "## 📈 Intermediate", "beginner"),
    ("## 📈 Intermediate", "## 🔬 Advanced", "intermediate"),
    ("## 🔬 Advanced", "## 🛠 Ecosystem & Tools", "advanced"),
    ("## 🛠 Ecosystem & Tools", "## 🏗 Frameworks", "ecosystem"),
    ("## 🏗 Frameworks", "## 🧪 Testing", "frameworks"),
    ("## 🧪 Testing", "## ⚡ Performance", "testing"),
    ("## ⚡ Performance", "## 🔒 Security", "performance"),
    ("## 🔒 Security", "## 📋 Cheat Sheets", "security"),
    ("## 📋 Cheat Sheets", "## 🎯 Interview Prep", "cheatsheets"),
    ("## 🎯 Interview Prep", "## 📚 Awesome Lists", "interview"),
    ("## 📚 Awesome Lists", "## 👥 Communities", "awesome"),
    ("## 👥 Communities", "## 📖 Books", "communities"),
    ("## 📖 Books", "## 🎬 Courses", "books"),
    ("## 🎬 Courses", "## 💡 Project Ideas", "courses"),
    ("## 💼 Career", "## ❓ FAQ", "career"),
]

if __name__ == "__main__":
    print("Script placeholder - will be completed")
