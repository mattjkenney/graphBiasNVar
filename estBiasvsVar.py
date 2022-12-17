def main():

    from matplotlib import pyplot as plt
    from pandas import DataFrame
    import numpy as np

    def get_data(pop_size, train_size):
        
        # Build initial dataset
        x = np.random.choice([0,1], size= pop_size)

        # Find Population Proportions
        df = DataFrame(x)
        p = df.value_counts(normalize=True, dropna=True)
        
        # Find Sample Proportions
        x = list(x)
        samples = [x.pop(np.random.randint(0, len(x))) for i in range(train_size)]
        dfs = DataFrame(samples)
        s = df.value_counts(normalize=True, dropna=True)

        return p, s
    
    pop_size = [1000, 2]
    train_size_p = 0.01
    train_size = int(train_size_p * pop_size[0])
    Ebs = []
    Var = []

    n = 2
    xs = []
    for i in range(15):
        step = n + i
        pop_size[-1] = step
        p, s = get_data(pop_size, train_size)
        Ebs.append(np.mean(s.values) - np.mean(p.values))
        Var.append(np.var(s.values))
        xs.append(step)

    xs = [i + 1 for i in range(len(Ebs))]
    
    plt.plot(xs, Ebs, label='Estimate Bias')
    plt.plot(xs, Var, label='Variance')
    plt.xticks(xs)
    plt.xlabel('Number of Edges (n)')
    plt.legend()
    plt.show()
        
main()
