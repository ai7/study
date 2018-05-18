
char* reverseString(char* s) {
    int n = strlen(s);
    for (int i = 0, j = n-1; i < j; i++, j--) {
        char t = s[i];
        s[i] = s[j];
        s[j] = t;
    }
    return s;
}
