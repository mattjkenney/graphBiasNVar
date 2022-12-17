def main(observations, train_size_p, edges_start, edges_end):

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
        s = dfs.value_counts(normalize=True, dropna=True)

        return p, s
    
    pop_size = [observations, 2]
    train_size = int(train_size_p * pop_size[0])
    Ebs = []
    Var = []

    n = edges_start
    xs = []
    for i in range(edges_end):
        step = n + i
        pop_size[-1] = step
        p, s = get_data(pop_size, train_size)
        eb = np.mean(s.values) - np.mean(p.values)
        print(eb)
        Ebs.append(eb)
        Var.append(np.var(s.values))
        xs.append(step)
    
    plt.plot(xs, Ebs, label='Estimate Bias')
    plt.plot(xs, Var, label='Variance')
    plt.xticks(xs)
    plt.xlabel('Number of Edges (n)')
    plt.legend()
    plt.show()
        
main(observations=1000,
     train_size_p= 0.3,
     edges_start= 2,
     edges_end= 15)
