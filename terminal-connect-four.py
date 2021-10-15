# terminal-connect-four
# made by Fishfinger
import os

def main():
    # create field
    field_size = (7, 6)
    field = [ [0 for h in range(field_size[1])] for w in range(field_size[0]) ]

    player_turn = 1

    chars = [".", "@", "O"]

    def get_input(prompt):
        valid_input = False
        while not valid_input:
            user_input = input(prompt)
            try: user_input = int(user_input)
            except: continue
            if int(user_input) > 0 and int(user_input) < 8:
                return int(user_input)

    def draw_field(field_):
        for h in range(field_size[1]):
            print( "".join( [ chars[field_[w][5-h]] + " " for w in range(field_size[0]) ]) )

        print( " ".join( [str(i+1) for i in range(0, field_size[0])] ) )

    def place_chip(column, turn_):
        for i in range(field_size[1]):
            if field[column][i] == 0:
                field[column][i] = turn_
                break

    def switch_turn(turn_):
        return 2 if turn_ == 1 else 1

    def is_winning_list(list_):
        return all(i==chars[1] for i in list_) or all(i==chars[2] for i in list_)

    def check_win_loop(field_):
        # diagonal top left -> bottom right \
        print("\\")
        for y in range(0, 3):
            for x in range(0, 4):
                print(f"({x}, {y})") # debug
                
                print(str( [ (x+xy, y+xy) for xy in range(4) ] )) # debug

        # diagonal bottom left -> top right /
        print("/")
        for y in range(0, 3):
            for x in range(3, 7):
                print(f"({x}, {y})") # debug
                
                print(str( [ (6-xy, y+xy) for xy in range(4) ] )) # debug

        # horizontal left -> right _
        print("_")
        for y in range(0, 6):
            for x in range(0, 4):
                print(f"({x}, {y})") # debug
                
                print(str( [ (x+w, y) for w in range(0, 7) ] )) # debug

        # vertical top -> bottom |
        print("|")
        for y in range(0, 3):
            for x in range(0, 7):
                print(f"({x}, {y})") # debug
                
                print(str( [ (x, y+h) for h in range(0, 6) ] )) # debug

    check_win_loop(field)
    input()
    
    while True:
        # main game loop
        draw_field(field)
        print(f"Player Turn: {chars[player_turn]}")
        input_ = get_input("1 -> 7: ")
        place_chip(input_-1, player_turn)
        player_turn = switch_turn(player_turn)
        os.system("cls")

if __name__ == "__main__":
    main()