def parse_input(fname):
    with open(fname) as f:
        return [int(x) for x in f.read().splitlines()]

def next_secret(secret):
    a = secret*64
    a = secret^a
    secret = a%16777216
    a = secret//32
    a = secret^a
    secret = a%16777216
    a = secret*2048
    a = secret^a
    return a%16777216

secrets = parse_input("22.input")

total = 0
price_changes = {}
for secret in secrets:
    new_secret = secret
    price = secret%10
    price_change_history = [0]
    price_changes_local = {}
    for i in range(2000):
        new_secret = next_secret(new_secret)
        new_price = new_secret%10
        price_change_history.append(new_price-price)
        price = new_price
        if i > 2:
            price_change_history.pop(0)
            if not (tuple(price_change_history) in price_changes_local):
                price_changes_local[tuple(price_change_history)] = new_price
    for k, v in price_changes_local.items():
        if not k in price_changes:
            price_changes[k] = v
        else:
            price_changes[k] += v

    total += new_secret

max_bananas = max(price_changes.values())
print("Part 1:", total)
print("Part 2:", max_bananas)