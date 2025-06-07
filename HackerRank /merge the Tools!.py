def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        t = string[i:i+k]
        u = set()
        for j in t:
            if j not in u:
                print(j,end='')
                u.add(j)
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
