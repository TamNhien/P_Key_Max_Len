def tim_gia_tri_chuoi_max(dictionary):
    # Sử dụng max() với key là độ dài của key để tìm key có độ dài lớn nhất
    max_key = max(dictionary.keys(), key=lambda x: len(x) if isinstance(x, str) else 0, default=None)
    return dictionary[max_key] if max_key is not None else None

my_dict = {'abc': 123, 'defg': 456, 'hijkl': 789}
result = tim_gia_tri_chuoi_max(my_dict)
print("Giá trị của key có độ dài lớn nhất là:", result)

