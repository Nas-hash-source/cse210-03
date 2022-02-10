class TerminalService:
    # Added by Hector Olivares Tapia as result of cse210 assignment # 
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def _read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.
     Yves: I converted this method from public to private because we need to accomplish the requirement of the encapsulation
        Args: 
           self (TerminalService): An instance of TerminalService.
           prompt (string): The prompt to display on the terminal.

        Returns:
           string: The user's input as text.
        """
        return input(prompt)
    
               

    def _write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(f'\n\033[1;37;41m {text} \033[0m\n')
# Yves I also changed these methods to private because i made some
# modification parachite if not the game would not be funtional.
# these changes were made by Yves          