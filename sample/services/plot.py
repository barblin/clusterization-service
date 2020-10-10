import matplotlib.pyplot as plt


def plot(data):
    # pt = 1002
    plt.figure(figsize=(8, 6))
    col_map = {0: 'tab:grey', 1: 'tab:orange', 2: 'tab:red', 3: 'tab:blue', 4: 'tab:purple', 5: 'tab:green', 6: 'tab:cyan'}
    plt.scatter(data['feat-1'], data['feat-2'], alpha=0.8, s=1, color=[col_map[sample] for sample in data.labels])
    # plt.scatter(df['f1'], df['f2'], c=df['label'])
    # plt.scatter(data[pt,0], data[pt,1], marker='x', s=100, lw=4, color='r')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('feature 1', size=15, labelpad=10)
    plt.ylabel('feature 2', size=15, labelpad=10)
    plt.tight_layout()
    plt.show()


def plot_cluster(data, labels):
    plt.figure(figsize=(8, 6))
    plt.scatter(data['feat-1'], data['feat-2'], alpha=0.8, s=3, c=labels, cmap='Set2')
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('feature 1', size=15, labelpad=10)
    plt.ylabel('feature 2', size=15, labelpad=10)
    plt.tight_layout()
    plt.show()
