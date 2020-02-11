import main

if __name__ == '__main__':
    sol = main.Solution()
    v = 91
    print("testing " + str(v))
    is_semiprime = sol.run(v)
    print(is_semiprime)
