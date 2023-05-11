from matplotlib import pyplot as plt


def plot_scores(X_test, iteration, before_is_correct: bool, after_is_correct: bool, before_queries_score_source, after_queries_score_source, budget):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 6), dpi=130)

    __scatter_scores(X_test, before_is_correct, ax1)
    ax1.set_title(
        'Before pooling, fold {i}, accuracy: {score:.3f}'
        .format(i=iteration + 1, score=before_queries_score_source))

    __scatter_scores(X_test, after_is_correct, ax2)
    ax2.set_title(
        'After pooling ({n} queries), fold {i}, accuracy: {final_acc:.3f}'
        .format(n=budget, i=iteration + 1, final_acc=after_queries_score_source))


def __scatter_scores(X_test, is_correct: bool, ax):
    ax.scatter(X_test[:, 0][is_correct], X_test[:, 1][is_correct], c='g', marker='+', label='Correct', alpha=8 / 10)
    ax.scatter(X_test[:, 0][~is_correct], X_test[:, 1][~is_correct], c='r', marker='x', label='Incorrect', alpha=8 / 10)
    ax.legend(loc='lower right')