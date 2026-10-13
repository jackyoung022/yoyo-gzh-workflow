# Third-party notices and publishing checks

## gzh-design

`skills/gzh-design/` is derived from the local `gzh-design` skill. Its included license is GNU Affero General Public License v3.0 or later, reproduced in the repository root as `LICENSE`. Keep the license and the original copyright notice when redistributing this repository. A repository that distributes this combined work should be published under compatible AGPL-3.0-or-later terms.

## Human-writing

`skills/human-writing/` is synchronized from the local human-writing Skill (version recorded in `VERSION`). It is provided under the MIT License; the complete license and copyright notice are preserved in `skills/human-writing/LICENSE`. This replaces the previous Khazix writing module.

## Runtime and optional external skills

Codex's built-in imagegen capability and Skill are runtime dependencies and are not redistributed here. The optional `handdraw-style-prompter` numbered-style and layout library is also not bundled. Install its complete package separately when requesting numbered styles or layout IDs; YOYO v2 resolves its actual assets at runtime.

## YOYO character assets and guidance

`skills/yoyo-illustrations/assets/` contains the YOYO character reference images. Publish them only if you own the assets or have permission to redistribute them. Remove the assets and reference them privately if that is not the case.

## Credentials

No real credentials belong in this repository. Rotate any credential that has ever been committed or pasted into a public issue, then use the environment variables documented in `.env.example`.
