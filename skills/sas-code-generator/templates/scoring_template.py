# NumPy Inference Scoring Pattern
def score_data_linear(panel: dict, betas: list) -> float:
    pred = 0.0
    # Python loop accumulation (Rule 4)
    for varname, estimate in betas:
        pred += panel.get(varname, 0.0) * estimate
    return pred
