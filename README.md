# dashAI Sample Plugin

A minimal plugin for [dashAI](https://github.com/DashAISoftware/DashAI) to start from. It adds one
metric and one setting, and walks you through the whole path: setting up, writing, testing,
trying it in dashAI, releasing it and listing it in the plugin store.

## What it adds

| Component | Type | What it does |
| --- | --- | --- |
| `SampleErrorRate` | Metric | Share of samples a classifier got wrong (1 − accuracy). Lower is better. |

In its **Settings** tab you choose how many decimals the error rate is rounded to.

## The path at a glance

1. **Set up**: your copy of this template, and a Python environment where dashAI can be imported.
2. **Write** the plugin: `manifest.json` and your components.
3. **Test** the logic with `pytest`, without opening dashAI.
4. **Try it in dashAI**: drop the folder in the **Plugins** module.
5. **Release** it: push a tag; a workflow builds and signs the release.
6. **List it in the store**: a pull request to the store's index.

## 1. Set up

**Your copy.** Click **Use this template** on GitHub, then clone your new repository.

**An environment for your editor and your tests.** Your code imports dashAI
(`from DashAI.back.metrics...`), so your editor needs a Python environment where dashAI can be
imported, to autocomplete it and to run your tests:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install dashai pytest
```

Then choose `.venv` as the Python interpreter in your editor (VS Code: *Python: Select
Interpreter*).

> Plugin support arrives in the dashAI release after 0.10.0. Until then, use a clone of the
> dashAI repository and its environment as your interpreter.

**A dashAI to try it in.** The desktop app, or `python -m DashAI` from that environment.

This environment is only for your editor and your tests. dashAI never runs your plugin from it: it
keeps its own copy of the plugin and installs its dependencies in a folder of its own.

## 2. Write it

```text
manifest.json                   what the plugin is: id, version, components, settings
src/sample_plugin/
  error_rate.py                 the metric
  settings.py                   the settings (optional)
tests/test_error_rate.py        a test of the metric's logic
.github/workflows/release.yml   builds and signs each release
README.md                       dashAI shows it in the plugin's page
LICENSE
```

**`manifest.json`** describes the plugin. dashAI reads it before installing, without running any
code, to show what the plugin will add. Change at least:

- `id`: lowercase letters and digits joined by `-`, without `dashai`. It never changes: installing
  a plugin with an installed `id` replaces it.
- `name`, `description`, `authors` and `project_urls` (every link must be `https://`).
- `min_app_version`: the oldest dashAI your plugin works with.
- `components`: one entry per class, `"module:Class"` plus its type (`Model`, `Converter`,
  `Metric`, `Task`, `DataLoader`, `Explorer`, `GlobalExplainer`, `LocalExplainer`, `Optimizer`,
  `GenerativeModel` or `GenerativeTask`).
- `dependencies`: pip requirements, if your code needs libraries dashAI doesn't ship.

**Components** extend one of dashAI's base classes, as dashAI's own do. This one extends
`ClassificationMetric`.

**Import your own modules relatively** (`from .settings import Settings`): dashAI loads each plugin
in its own namespace and doesn't add it to `sys.path`.

**Settings** are optional: a class that extends `BasePluginSettings`, named in the manifest's
`settings`. Read them where you use them (`Settings.load()`), not when the module is imported.

## 3. Test the logic

```bash
pytest
```

The test checks `error_rate` directly, in a second, without dashAI running. Keep the logic of
your components in functions like this one and test them here: it is the fast loop. Trying it in
dashAI (step 4) checks what only dashAI can: that it installs, loads and shows up where it should.

## 4. Try it in dashAI

1. Open **Plugins → Install development plugin** and drop your plugin's folder (or a `.zip` of it).
2. The preview lists the components it will add, or what is wrong: an invalid manifest, a type
   that doesn't match the class, a name another plugin already uses, a module that can't be found.
3. Install it and use it: this metric shows up when you train a classification model.

**After each change, drop the folder again.** Same `id`, so it replaces the installed plugin,
without restarting dashAI, and the next job uses the new code.

## 5. Release it

```bash
git tag v1.0.1
git push origin v1.0.1
```

The workflow copies the tag into the manifest's `version`, builds the `.zip`, signs it with a
GitHub attestation and attaches it to the release. Anyone can now install your plugin from
**Plugins** by pasting your repository's URL, and dashAI shows it as verified: the file was built
from your repository at that tag.

Each release needs a higher version: users get it with **Update**, which only installs a newer
one.

## 6. List it in the store

dashAI's plugin store is a [GitHub repository](https://github.com/vicentzamoras/dashai-plugins)
with one file per plugin. Before opening the pull request, check that:

- your repository is public, with a license the store accepts (MIT, Apache 2.0, BSD 2/3, GPLv3,
  LGPLv3, Unlicense) and a `README.md` at its root;
- your release installs in dashAI from your repository's URL;
- your `id` is not taken and doesn't contain `dashai`.

Then open a pull request, from your GitHub account (the owner of the plugin's repository), that
adds **`plugins/<id>.json`** (the `.json` extension is required) and nothing else:

```json
{ "id": "sample-plugin", "repo": "your-user/your-repository" }
```

A bot checks your entry, your repository and your releases, and its summary says what to fix if
something fails. A person of the dashAI team reviews it and merges it, and your plugin appears in
the store. New releases need no other pull request: the store picks them up within a day.

More in the store's [CONTRIBUTING.md](https://github.com/vicentzamoras/dashai-plugins/blob/main/CONTRIBUTING.md).
