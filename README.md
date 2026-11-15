# Destructive Action Guard (`destructive-action-guard`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Sponsor Vikyek](https://img.shields.io/badge/Sponsor-GitHub-ea4aaa?logo=github-sponsors&logoColor=white)](https://github.com/sponsors/Vikyek)

An open-source, cross-agent `SKILL.md` safety gate that halts irreversible Git, GitHub, filesystem, and system actions until the agent inspects read-only state, presents an exact blast-radius summary, and receives **typed target confirmation** from the user.

---

## 🛡️ Guarded Actions

- **GitHub / Remote:** `gh repo delete`, `gh repo archive`, `gh api -X DELETE` on repos/secrets/environments
- **Git History:** `git push --force`, `git filter-repo`, `git reset --hard`, `git clean -fdx`, `git branch -D` on unmerged branches
- **Filesystem:** `rm -rf` on project roots, config directories, or wildcards
- **System & Data:** `paru -Rns` / `pacman -Rdd` on core packages, `mkfs`, `dd`, `DROP` / `TRUNCATE`

---

## 🛠️ Installation

### Quick Install Script

```bash
./install.sh
```

By default, `install.sh` symlinks `SKILL.md` into `~/.gemini/config/skills/destructive-action-guard/SKILL.md` (pass `--target <dir>` for `~/.agents/skills` or `~/.claude/skills`).

### Manual Installation

```bash
mkdir -p ~/.gemini/config/skills/destructive-action-guard
ln -sf "$(pwd)/SKILL.md" ~/.gemini/config/skills/destructive-action-guard/SKILL.md
```

For workspace-only activation, symlink into `<workspace>/.agents/skills/destructive-action-guard/SKILL.md`.

---

## 🧪 Verification

```bash
pytest -q
```

---

## Support & Sponsorship

`destructive-action-guard` is authored and maintained by **[Vikyek](https://github.com/Vikyek)** as an independent open-source project. Everything is 100% open-source, telemetry-free, and public.

<div align="center">

[![Sponsor Vikyek](https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?logo=github&style=for-the-badge)](https://github.com/sponsors/Vikyek)
[![Donate on Liberapay](https://img.shields.io/badge/Donate-Liberapay-f6c915?style=for-the-badge&logo=liberapay&logoColor=black)](https://liberapay.com/Vikyek)
[![Sponsor on Polar](https://img.shields.io/badge/Sponsor-Polar-0062FF?style=for-the-badge&logo=polar&logoColor=white)](https://polar.sh/vikyek)
[![Donate with Stripe](https://img.shields.io/badge/Donate-Stripe-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://profile.stripe.com/@vikyek)

</div>

> ### 🎯 Active Sponsorship Goal: Monthly Living Essentials
> **Target:** **2,710 PLN / ~$680 USD per month** (`630 PLN / week`) — Rent & Essential Utilities  
> Covering basic living essentials directly unlocks dedicated, sustainable full-time independent open-source engineering across Arch Linux utilities, developer tools, and AI middleware free from corporate telemetry, ads, or paywalls.

If `destructive-action-guard` helps safeguard your development workflow, consider supporting ongoing work:

- **GitHub Sponsors**: [github.com/sponsors/Vikyek](https://github.com/sponsors/Vikyek) *(Monthly tiers and one-time tips)*
- **Liberapay**: [liberapay.com/Vikyek](https://liberapay.com/Vikyek) *(0% platform fee recurrent patronage in EUR/USD/PLN)*
- **Polar**: [polar.sh/vikyek](https://polar.sh/vikyek) *(Developer subscriptions & commercial passes)*
- **Direct Stripe Profile**: [profile.stripe.com/@vikyek](https://profile.stripe.com/@vikyek) *(Direct one-time tips & sponsorship)*

Every contribution—monthly or one-time—directly supports active maintenance, hardware testbeds, and new feature development!

---

## 🌐 Ecosystem

Part of the **[Vikyek](https://github.com/Vikyek)** developer tooling and AI agent middleware ecosystem:

| Project | Description |
|---|---|
| **[toon-mcp](https://github.com/Vikyek/toon-mcp)** | FastMCP server & CLI for token-efficient TOON format serialization |
| **[vorchestrator](https://github.com/Vikyek/vorchestrator)** | Multi-agent orchestration, dynamic tiering & dual-provider quota optimizer |
| **[agy-input-wrap](https://github.com/Vikyek/agy-input-wrap)** | Clean PTY terminal input interceptor & prompt optimizer for AI CLIs |
| **[destructive-action-guard](https://github.com/Vikyek/destructive-action-guard)** | Blast-radius guard & safety interception engine for autonomous agents |
| **[paru-wrapper](https://github.com/Vikyek/paru-wrapper)** | Enhanced Arch Linux pacman/paru wrapper with plugins & hook lifecycle |
| **[vlfstatus](https://github.com/Vikyek/vlfstatus)** | Ultra-lightweight, modular status bar generator for Linux desktops |

---

## 📄 License

MIT © [Vikyek](https://github.com/Vikyek)
