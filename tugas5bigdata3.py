import csv
from functools import reduce

def mapper(namafile):
    mapped_values = []
    with open(namafile, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            berat = float(row["berat badan"])
            mapped_values.append((berat, 1))
    return mapped_values

def reducer_sum(values):
    total_sum = reduce(lambda x, y: x + y[0], values, 0)
    total_count = reduce(lambda x, y: x + y[1], values, 0)
    return total_sum, total_count

def reducer_rata2(sum_count_pair):
    total_sum, total_count = sum_count_pair
    rata2 = total_sum / total_count
    return rata2

def main():
    mapped_values = mapper('C:/Users/user/Documents/Big Data/beratbadan.csv')

    sum_count_pair = reducer_sum(mapped_values)
    print(f"Total berat badan dari {sum_count_pair[1]} orang : {sum_count_pair[0]}")

    rata2 = reducer_rata2(sum_count_pair)
    print(f"Rata-rata berat badan dari {sum_count_pair[1]} orang : {rata2}")

if __name__ == "__main__":
    main()
