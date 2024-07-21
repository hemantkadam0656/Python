# import textwrap

# def wrap(string, max_width):    
#     return "\n".join(textwrap.wrap(string, width=max_width))

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


N, M = map(int, input().split())

# pattern = [(".|."* i).center(M, "-") for i in range(1, N)]
for i in range(1,N):
    pattern = (".|."*i).center(N,"-")

print("\n".join(pattern+["WELCOME".center(N, "-")]+pattern[::-1]))

