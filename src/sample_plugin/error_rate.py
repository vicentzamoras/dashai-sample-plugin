"""A classification metric: the share of samples the model got wrong."""

from DashAI.back.core.utils import MultilingualString
from DashAI.back.metrics.classification_metric import (
    ClassificationMetric,
    prepare_to_metric,
)

# Your own modules are imported relatively: dashAI loads each plugin in its
# own namespace and does not add it to sys.path.
from .settings import Settings


class SampleErrorRate(ClassificationMetric):
    """1 - accuracy: lower is better."""

    MAXIMIZE = False
    DISPLAY_NAME = MultilingualString(
        en="Error Rate (sample)", es="Tasa de error (ejemplo)"
    )
    DESCRIPTION = MultilingualString(
        en="Share of samples classified wrongly. Lower is better.",
        es="Proporción de muestras mal clasificadas. Menor es mejor.",
    )

    @staticmethod
    def score(true_labels, probs_pred_labels) -> float:
        true_labels, pred_labels = prepare_to_metric(true_labels, probs_pred_labels)
        error_rate = float((true_labels != pred_labels).mean())
        # Read the settings when used, not when the module is imported: the
        # job worker keeps running and picks up a change at its next job.
        return round(error_rate, Settings.load().decimals)
