import numpy as np

def eliminacao_gauss(m):
    for i in range(0, m.shape[0]-1):
        sub = m[i+1:, i] / m[i][i]
        for j in range(i, m.shape[0]-1):
            m[j+1, :] = m[j+1, :] - sub[j-i]*m[i, :]

    x = []
    for i in range(m.shape[0]-1, -1, -1):
        x.append((m[i][-1] - np.sum(m[i, i+1:-1])) / m[i][i])
        m[:, i] *= x[-1]

    return np.flip(x)

def main():
    input_txt = open('input-eliminacao.txt', 'r')
    output_txt = open('output-eliminacao.txt', 'w')
    np.set_printoptions(precision=6)
    np.set_printoptions(suppress=True)

    m = []
    for line in input_txt:
        if line[-1] == '\n':
            line = line[:-1]
        m.append(line.split(" "))
        m[-1] = list(map(lambda x: float(x), m[-1]))

    m = np.asarray(m)
    m[:, :-1] = np.linalg.inv(m[:, :-1])
    print(m[:, :-1])
    x = eliminacao_gauss(np.copy(m))
    output_txt.write(str(x)+"\n")

    m[:, :-1] *= x
    n = np.sum(m[:, :-1], axis=1)
    n = np.abs(m[:,-1]-n)

    output_txt.write(str(n)+"\n")

    input_txt.close()
    output_txt.close()

main()