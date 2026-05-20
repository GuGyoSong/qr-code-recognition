def parse_qr(qr_list):

    has_a = False
    has_b = False
    has_c = False
    delivery_slot = 0

    for q in qr_list:
        q = q.lower()

        # 样本标记
        if "a" in q:
            has_a = True
        if "b" in q:
            has_b = True
        if "c" in q:
            has_c = True

        # 检测类型
        if "blood" in q:
            delivery_slot = 1
        elif "fluid" in q:
            delivery_slot = 2
        elif "immune" in q:
            delivery_slot = 3
        elif "hormone" in q:
            delivery_slot = 4

    return has_a, has_b, has_c, delivery_slot
