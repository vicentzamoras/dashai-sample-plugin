# dashAI Sample Plugin

A minimal plugin for [dashAI](https://github.com/DashAISoftware/DashAI) to start from. It adds one
metric, **Error Rate (sample)**, and one setting, so you can see every piece a plugin has.

## What it adds

| Component | Type | What it does |
| --- | --- | --- |
| `SampleErrorRate` | Metric | Share of samples a classifier got wrong (1 − accuracy). Lower is better. |

In its **Settings** tab you choose how many decimals the error rate is rounded to.

## Structure

```text
manifest.json                 what the plugin is: id, version, components, settings
src/sample_plugin/
  error_rate.py               the metric
  settings.py                 the settings
.github/workflows/release.yml builds and signs the release's .zip
README.md                     this file: dashAI shows it in the plugin's page
LICENSE
```

dashAI reads `manifest.json` before installing, without running any code, to show what the plugin
will add. Each component is `module:Class` plus its type.

## Make your own

1. Click **Use this template** on GitHub to get your own copy.
2. In `manifest.json`, change `id` (lowercase letters and digits joined by `-`, without `dashai`),
   `name`, `description`, `authors` and the links.
3. Replace the metric with your components. A component extends one of dashAI's base classes
   (`BaseModel`, `BaseConverter`, `BaseMetric`…) and goes in `components` with its type.
4. Import your own modules relatively (`from .settings import Settings`).

## Try it

1. Compress the folder into a `.zip`.
2. In dashAI, open **Plugins → Install development plugin** and drop the `.zip` (or the folder).
3. Review the preview and install it. The metric shows up when you train a classification model.

Uploading a new `.zip` with the same `id` replaces the installed one.

## Publish a release

Push a tag:

```bash
git tag v1.0.1
git push origin v1.0.1
```

The workflow copies the tag into `version`, builds the `.zip`, signs it with a GitHub attestation
and attaches it to the release. Anyone can then install the plugin from **Plugins** by pasting
your repository's URL, and dashAI shows it as **Verified**.

## Publish it in the store

To list it in dashAI's plugin store, open a pull request to the
[store's index](https://github.com/vicentzamoras/dashai-plugins) that adds `plugins/<id>.json`.
Its [CONTRIBUTING.md](https://github.com/vicentzamoras/dashai-plugins/blob/main/CONTRIBUTING.md)
explains the checks.
