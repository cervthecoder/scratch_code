def sort(li_st):
    [li_st.append(li_st.pop(0) if i == len(li_st) - 1 or li_st[0] < li_st[1] else li_st.pop(1)) for j in range(0, len(li_st)) for i in range(0, len(li_st))]
    return li_st

print(sort([3, 2, 1]))

