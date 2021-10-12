import numpy as np

target = 80
score_beg = np.array([72, 35, 64, 88, 51, 90, 74, 12])


def curve(score_beg):
	limit_up = 100
	mean_score = score_beg.mean()
	added_score = target - mean_score
	new_score = score_beg + added_score
	return np.clip(new_score, score_beg, limit_up)


print(score_beg)
curve(score_beg)
