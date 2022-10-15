def pi_function(s: list = "&&&&vv&&advvv&&&"):
    """pi-functions returns the max string own suffix which is in turn its prefix
    (maximum string suffix cannot be equal to string)
    complexity is O(len(s))"""
    pi = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        p = pi[i - 1]
        while p > 0 and s[i] != s[p]:
            p = pi[p - 1]
        if s[i] == s[p]:
            p += 1
        pi[i] = p
    return pi


def kmp(s="aueqdasdsaueqdahdksdakhueqdkjasgdkqwe", sub="ueq"):
    """ Algorythm of Knutt-Morris-Pratt to find substring in string based on pi-function.
    Complexity is O(len(s)+len(sub)).Key contrain = string and substring should not contain "#" special symbol
    retruns all starting indexes of substring in string
    """
    sub_l = len(sub)
    pi = pi_function(sub + '+' + s)
    indexes = []
    for i in range(len(pi)):
        if pi[i] == sub_l:
            indexes.append(i - 2 * sub_l)
    return indexes


def read_file(f='./pythonstudy/denis_automation_export_prb_sys_audit_1.json'):
    with open(f) as json_file:
        s = json_file.read()
    json_file.close()
    return s


if __name__ == "__main__":
    f = read_file()
    #    print(f[1925182:1927182])
    #    print(f[1925118:1927182])
    print(f[15251000:15253370])
#    print(*kmp(s=f,sub='6e5687921b4a009c0ee12fc4bd4bcb52'))
