def binSearch(si, ei, L, SE):
    if si<=ei:
        mi = (si+ei)//2
        if SE == L[mi]:
            return True, mi
        elif SE < L[mi]:
            return binSearch(si, mi-1, L, SE)
        else:
            return binSearch(mi+1, ei, L, SE)
    else:
        return False, None