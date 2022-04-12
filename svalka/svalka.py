


new_line = ['--s!!---da???', '№№№--!!--!!', '!s--ad!!']
line_exception1 = ('!',  '\"', '.', ',', '?', ':', ';', '\'', '-', '(', ')', '[', ']', '#', '№')
for element1 in line_exception1:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].rfind(element1) == (len(new_line[counter]) - 1):
            new_line[counter] = new_line[counter][:-1]
            continue
        elif new_line[counter].find(element1) == 0:
            new_line[counter] = new_line[counter][1:]
            continue
        else:
            counter += 1


line_exception2 = ('\'', '-')
for element2 in line_exception2:
    counter = 0
    while not counter > len(new_line) - 1:
        if len(new_line[counter]) == 0:
            counter += 1
            continue
        elif new_line[counter].find(element2) != -1:
            slice_index = new_line[counter].find(element2)
            new_line[counter] = new_line[counter][:slice_index] + new_line[counter][slice_index+1:]
            continue
        else:
            counter += 1

print(new_line)          
