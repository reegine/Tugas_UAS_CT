def end_story():
    animate_text("STORY FINALIZED")
    choice = get_user_choice("Do you want to restart the game? (yes/no): ", ['yes', 'no'])
    if choice == 'yes':
        main()
    elif choice == 'no':
        exit()