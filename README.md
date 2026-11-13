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
[![Donate with Stripe](https://img.shields.io/badge/Donate-Stripe-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://profile.stripe.com/@vikyek)

</div>

> ### 🎯 Active Sponsorship Goal: Monthly Living Essentials
> **Target:** **2,710 PLN / ~$680 USD per month** (`630 PLN / week`) — Rent & Essential Utilities  
> Covering basic living essentials directly unlocks dedicated, sustainable full-time independent open-source engineering across Arch Linux utilities, developer tools, and AI middleware free from corporate telemetry, ads, or paywalls.
