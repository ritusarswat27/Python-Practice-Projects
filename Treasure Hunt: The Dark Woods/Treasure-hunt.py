title = "The Lost Treasure of Shadow Forest."
print(title, delay=0.05)

while True: 
    scene_1 = "You wake up at the edge of Shadow Forest, known for its secrets. A narrow trail splits into two paths."
    print(scene_1, delay=0.05)
    while True:  
            user = input("Do you go left or right?: ").lower()
            if user == "right":
                scene_2 = "You walk deeper into a dense area and suddenly hear a growl. A bear appears"
                print(scene_2, delay=0.05)
                while True: #Bear Choice loop
                    user_bear = input("Do you run or climb a tree?: ").lower()
                    if user_bear == "run":
                        scene_41 = "You trip over a root. The bear sniffs you, but walks away. You spot a hidden cabin nearby."
                        print(scene_41, delay=0.05)
                        while True: #cabin choice loop
                            user_cabin = input("Do you enter or walk past it?: ").lower()
                            if user_cabin == "enter":
                                scene_61 = "You find a diary with clues to a treasure.\n You Win (Clue Ending)!"
                                print(scene_61, delay=0.05)
                                break  
                            elif user_cabin == "walk past":
                                scene_81 = "You get lost in the forest.\nGame Over."
                                print(scene_81, delay=0.05)
                                break  
                            else:
                                print("Invalid choice. Enter 'enter' or 'walk past'.")
                        break  
                    elif user_bear == "climb a tree":
                        scene_42 = "You’re safe... but stuck! After hours, you hear a hiker’s voice."
                        print(scene_42, delay=0.05)
                        while True:  
                            user_hiker = input("Do you call for help or stay silent?: ").lower()
                            if user_hiker == "call for help":
                                scene_62 = "The hiker helps you down and shares survival tips.\n You survive. You Win (Survivor Ending)!"
                                print(scene_62, delay=0.05)
                                break  
                            elif user_hiker == "stay silent":
                                scene_82 = "You fall asleep, lose balance, and fall.\nGame Over."
                                print(scene_82, delay=0.05)
                                break  
                            else:
                                print("Invalid choice. Enter 'call for help' or 'stay silent'.")
                        break  
                    else:
                        print("Invalid choice. Enter 'run' or 'climb'.")
                break  

            elif user == "left":
                scene_3 = "You walk into thick fog. After a few minutes, you reach a wide river."
                print(scene_3, delay=0.05)
                while True:  
                    user_river = input("Do you try to swim across or build a raft?: ").lower()
                    if user_river in ["swim"]:
                        scene_51 = "The current is strong. Halfway through, you see something shiny under water"
                        print(scene_51, delay=0.05)
                        while True:  
                            user_dive = input("Do you dive or keep swimming?: ").lower()
                            if user_dive in ["dive"]:
                                scene_71 = "It's a treasure chest! But you run out of breath. Game Over."
                                print(scene_71, delay=0.05)
                                break  
                            elif user_dive in ["keep swimming", "keep_swimming", "swimming", "keep"]:
                                scene_91 = "You reach the shore safely. You find an ancient map lying on a rock.\n You Win (Map Ending)!"
                                print(scene_91, delay=0.05)
                                break  
                            else:
                                print("Invalid choice. Choose 'dive' or 'keep swimming'.")
                        break  
                    elif user_river in ["build", "build a raft", "build_a_raft", "raft"]:
                        scene_52 = "You build a raft. Midway, it starts falling apart."
                        print(scene_52, delay=0.05)
                        while True:  
                            user_fix = input("Do you jump into the water or try to fix it?: ").lower()
                            if user_fix in ["jump"]:
                                scene_72 = "You safely swim back. But you’re back where you started. Try again!"
                                print(scene_72, delay=0.05)
                                break  
                            elif user_fix in ["try to fix", "try_to_fix", "try", "fix"]:
                                scene_92 = "Your raft holds! You reach a hidden cave with glowing crystals.\n You Win (Cave Ending)!"
                                print(scene_92, delay=0.05)
                                break  
                            else:
                                print("Invalid choice. Choose 'jump' or 'try to fix'.")
                        break  
                    else:
                        print("Invalid choice. Choose 'swim' or 'build a raft'.")
                break  
            else:
                print("Invalid choice. Enter 'left' or 'right'.") 

    replay_game = input("Do you want to play again? (yes/no): ").lower()
    if replay_game not in ["yes", "y"]:
        print("Thanks for playing... Goodbye!")
        break