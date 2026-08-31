# Assignment 7.1
# Weicheng Huang

# libraries


# functions
def compress_strand(strand):
    strand_list = []
    pos = 0
    for index in range(len(strand)):
        try:
            if strand[index] != strand[index + 1] and index + 1 != len(strand):
                if pos == 0:
                    temp_tuple = (strand[index], index + 1 - pos)
                else:
                    temp_tuple = (strand[index], index - pos)
                strand_list.append(temp_tuple)
                pos = index
                index += 1
        except IndexError:
            temp_tuple = (strand[index], index-pos)
            strand_list.append(temp_tuple)
            break
        
    return strand_list

def uncompress_strand(strand_list):
    strand_string = ""
    for index in range(len(strand_list)):
        temp_tuple = strand_list[index]
        num = temp_tuple[1]
        while num > 0:
            strand_string += temp_tuple[0]
            num -= 1
        
    return strand_string

def combine_nucleotides(strand_list, index):
    try:
        temp_tuple1 = strand_list[index]
        temp_tuple2 = strand_list[index + 1]
        if temp_tuple1[0] == temp_tuple2[0]:
            temp_tuple3 = (temp_tuple1[0], temp_tuple1[1] + temp_tuple2[1])
            strand_list.pop(index + 1)
            strand_list[index] = (temp_tuple3)
            
    except IndexError:
        return
    
def ligate(list1, list2):
    combined_list = list1 + list2

    for index in range(len(combined_list)):
        try:
            temp_tuple1 = combined_list[index]
            temp_tuple2 = combined_list[index + 1]
            if temp_tuple1[0] == temp_tuple2[0]:
                combine_nucleotides(combined_list, index)
        except IndexError:
            break

    return combined_list

def delete(strand_list, start, stop):
    times = stop - start
    
    while times >= 0:
        strand_list.pop(start+times)
        times -= 1

def splice(list1, list2, index):
    slice1 = list1[:index]
    slice2 = list1[index:]
    new_list = slice1 + list2 + slice2

    for index in range(len(new_list)):
        try:
            temp_tuple1 = new_list[index]
            temp_tuple2 = new_list[index + 1]
            if temp_tuple1[0] == temp_tuple2[0]:
                combine_nucleotides(new_list, index)
        except IndexError:
            break

    return new_list

# main
def main():
    strand = ""
    cstrand = []
    valid_strand = False
    
    while valid_strand != True:
        strand = input("Enter a DNA Strand: ")
        for index in range(len(strand)):
            if strand[index] != 'A' and strand[index] != 'C' and strand[index] != 'T' and strand[index] != 'G':
                print(strand[index])
                print("Invalid Nucleotides in DNA Strand")
                print("Please try again")
                valid_strand = False
                break
            elif index == range(len(strand)) and strand[index] == 'A' or strand[index] == 'C' or strand[index] == 'T' or strand[index] == 'G':
                valid_strand = True
                cstrand = compress_strand(strand)
            else: 
                continue

    command = ''
    command = input("> ")
    cmd = command.split(' ')
    while command != 'q':
        if cmd[0] == 'h':
            print("h - this help menu")
            print("l <dna_strand> - append this DNA strand to the current strand")
            print("d <start_index> <end_index> - delete nucleotides between <start_index>")
            print("s <dna_strand> <index> - splice this DNA strand into the current strand at the given index")
            print("q - quit")
            print(cstrand)
            print(strand)
        elif cmd[0] == 'l':
            new_strand = cmd[1]
            for index in range(len(new_strand)):
                if new_strand[index] != 'A' and new_strand[index] != 'C' and new_strand[index] != 'T' and new_strand[index] != 'G':
                    print("Invalid DNA strand entered. Try again.")
                    print(cstrand)
                    print(strand)
                    break
                else:
                    ligate_strand = compress_strand(cmd[1])
                    cstrand = ligate(cstrand, ligate_strand)
                    strand = uncompress_strand(cstrand)
                    print(cstrand)
                    print(strand)
                    break
        elif cmd[0] == 'd':
            start = int(cmd[1])
            stop = int(cmd[2])
            delete(cstrand, start, stop-1)
            strand = uncompress_strand(cstrand)
            print(cstrand)
            print(strand)
        elif cmd[0] == 's':
            splice_strand = compress_strand(cmd[1])
            index = int(cmd[2])
            # knwon error: Duplicates the letter T one extra from input
            # Status: Unresolved
            cstrand = splice(cstrand, splice_strand, index)
            strand = uncompress_strand(cstrand)
            print(cstrand)
            print(strand)
        elif cmd[0] == 'q':
            break
        else:
            print("Please input valid command")
        command = input("> ")
        cmd = command.split(' ')
    print("Goodbye")



main()