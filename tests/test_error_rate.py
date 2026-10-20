from sample_plugin.error_rate import error_rate


def test_counts_the_wrong_predictions():
    assert error_rate([0, 1, 1, 0], [0, 1, 0, 0]) == 0.25
