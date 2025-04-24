import kivy
kivy.require('2.1.0') # Specify your Kivy version if needed

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp # Import dp for explicit sizing
import math # Needed for math functions
import re   # Needed for regular expression substitution

# --- Kivy Language String ---
# (KV_STRING remains the same as the previous version with % button)
KV_STRING = """
#:set color_bg (0.85, 0.85, 0.85, 1)        # Light grey background
#:set color_input_bg (1, 1, 1, 1)           # White input background
#:set color_text_dark (0.1, 0.1, 0.1, 1)      # Dark text
#:set color_text_light (1, 1, 1, 1)     # White text
#:set color_btn_num (0.2, 0.2, 0.2, 1)      # Dark grey for numbers (#333333)
#:set color_btn_op (0.95, 0.95, 0.95, 1)    # Lighter grey for operators
#:set color_btn_util_white (1, 1, 1, 1)     # White for ()%
#:set color_btn_util_blue (0.2, 0.6, 1, 1)   # Blue for AC/DEL
#:set color_btn_equal (0.56, 0.93, 0.56, 1) # Light green for =
#:set color_btn_brand (0.68, 0.85, 0.9, 1)   # Light blue for brand

<CalculatorLayout>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: color_bg
        Rectangle:
            pos: self.pos
            size: self.size

    expression_input: expression_input # Link Python property
    result_label: result_label         # Link Python property

    # --- Input and Result Area ---
    TextInput:
        id: expression_input
        font_size: '24sp'
        multiline: False
        halign: 'right'
        padding: [dp(10), (self.height - self.line_height) / 2] # Pad L/R, center V
        size_hint_y: 0.15 # Relative height
        background_color: color_input_bg
        foreground_color: color_text_dark

    Label:
        id: result_label
        text: ""
        font_size: '20sp'
        color: color_text_dark
        canvas.before:
            Color:
                rgba: color_input_bg # White background like sunken label
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: color_bg # Border color
            Line:
                width: dp(1.5)
                rectangle: self.x, self.y, self.width, self.height
        size_hint_y: 0.15 # Relative height
        text_size: self.width - dp(10), self.height # Enable wrapping
        halign: 'right'
        valign: 'middle'
        padding: dp(10), dp(10)

    # --- Top Utility Buttons ---
    GridLayout:
        cols: 5
        spacing: dp(1)
        size_hint_y: 0.1 # Small fixed height proportion
        Button:
            text: '('
            on_press: root.add_to_expression('(')
            background_normal: ''
            background_color: color_btn_util_white # Changed color
            color: color_text_dark # Changed text color for white bg
            font_size: '18sp'
        Button:
            text: ')'
            on_press: root.add_to_expression(')')
            background_normal: ''
            background_color: color_btn_util_white # Changed color
            color: color_text_dark # Changed text color for white bg
            font_size: '18sp'
        Button:
            text: '%' # Changed from !
            on_press: root.add_to_expression('%') # Changed from !
            background_normal: ''
            background_color: color_btn_util_white # Changed color
            color: color_text_dark # Changed text color for white bg
            font_size: '18sp'
        Button:
            text: 'DEL'
            on_press: root.backspace()
            background_normal: ''
            background_color: color_btn_util_blue # Changed color
            color: color_text_light # Changed text color for blue bg
            font_size: '18sp'
        Button:
            text: 'AC'
            on_press: root.clear_expression()
            background_normal: ''
            background_color: color_btn_util_blue # Changed color
            color: color_text_light # Changed text color for blue bg
            font_size: '18sp'

    # --- Branding Button ---
    Button:
        text: 'Subhankar Dakua'
        # No on_press needed
        background_normal: ''
        background_color: color_btn_brand
        color: color_text_dark
        font_size: '14sp'
        spacing: dp(290)
        size_hint_y: 0.10# Small fixed height proportion

    # --- Main Area: Numbers (Left) + Operators/Equals (Right) ---
    BoxLayout:
        orientation: 'horizontal'
        spacing: dp(2)
        size_hint_y: 0.52# Remaining vertical space

        # --- Left Side: Number Pad ---
        GridLayout:
            cols: 3
            spacing: dp(1)
            size_hint_x: 4# Takes 75% of the horizontal space

            # Numbers 7 down to . (styling remains same)
            Button:
                text: '7'
                on_press: root.add_to_expression('7')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '8'
                on_press: root.add_to_expression('8')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '9'
                on_press: root.add_to_expression('9')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '4'
                on_press: root.add_to_expression('4')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '5'
                on_press: root.add_to_expression('5')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '6'
                on_press: root.add_to_expression('6')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '1'
                on_press: root.add_to_expression('1')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '2'
                on_press: root.add_to_expression('2')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '3'
                on_press: root.add_to_expression('3')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '0'
                on_press: root.add_to_expression('0')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '00'
                on_press: root.add_to_expression('00')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'
            Button:
                text: '.'
                on_press: root.add_to_expression('.')
                background_normal: ''
                background_color: color_btn_num
                color: color_text_light
                font_size: '18sp'

        # --- Right Side: Operators and Equals ---
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(2)
            size_hint_x: 3# Takes 25% of the horizontal space

            # --- 2x2 Grid for Operators ---
            GridLayout:
                cols: 2
                spacing: dp(1)
                size_hint_y: 2# Relative height within this BoxLayou

                Button:
                    text: '÷' # Display symbol
                    on_press: root.add_to_expression('/') # Use '/' internally
                    background_normal: ''
                    background_color: color_btn_op
                    color: color_text_dark
                    font_size: '22sp' # Increased font size
                Button:
                    text: '*'
                    on_press: root.add_to_expression('*')
                    background_normal: ''
                    background_color: color_btn_op
                    color: color_text_dark
                    font_size: '22sp' # Increased font size
                Button:
                    text: '-'
                    on_press: root.add_to_expression('-')
                    background_normal: ''
                    background_color: color_btn_op
                    color: color_text_dark
                    font_size: '22sp' # Increased font size
                Button:
                    text: '+'
                    on_press: root.add_to_expression('+')
                    background_normal: ''
                    background_color: color_btn_op
                    color: color_text_dark
                    font_size: '22sp' # Increased font size

            # --- Equals Button ---
            Button:
                text: '='
                on_press: root.calculate() # Trigger calculation
                background_normal: ''
                background_color: color_btn_equal
                color: color_text_dark
                font_size: '35sp' # Keep equals font size standard or increase if desired
                size_hint_y: 2 # Relative height within this BoxLayout
"""


# --- Kivy Root Widget ---
class CalculatorLayout(BoxLayout):
    expression_input = ObjectProperty(None)
    result_label = ObjectProperty(None)

    # --- Preprocessing Functions ---
    def preprocess_percentage(self, expression):
        """
        Processes percentage calculations based on common calculator logic.
        Handles:
            Y + X% -> Y + (Y*X/100)
            Y - X% -> Y - (Y*X/100)
            Other X% -> (X/100) (e.g., for multiplication, division, standalone)

        Limitations:
            - Does not correctly handle negative numbers within percentage terms (e.g., 100 + -10%).
            - Does not handle percentages applied directly to parenthesized expressions e.g. (10+5)%.
            - Assumes standard order of operations; complex chained percentages might require a full parser.
        """
        processed = expression
        # Regex Explanation:
        # (\d+\.?\d*) : Capture group 1: One or more digits, optionally followed by a decimal point and more digits (the number Y or X).
        # \s* : Zero or more whitespace characters.
        # ([+-])      : Capture group 2: Either a '+' or a '-' sign.
        # ([*/])      : Capture group 2: Either a '*' or a '/' sign.
        # %           : The literal percentage sign.

        # Pattern for Y + X% or Y - X%
        # We capture Y (group 1), the operator (group 2), and X (group 3)
        pattern_add_sub = r'(\d+\.?\d*)\s*([+-])\s*(\d+\.?\d*)\s*%'
        # Pattern for standalone X% or X% in other contexts (like *, /)
        # We capture X (group 1)
        pattern_other = r'(\d+\.?\d*)\s*%'

        # --- Handle Add/Subtract cases first (repeatedly) ---
        # Loop necessary for cases like 100 + 10% + 5%
        while True:
            original_processed = processed
            # Replace Y op X% with Y op (Y*X/100)
            # Note: \1 refers to capture group 1 (Y), \2 to group 2 (op), \3 to group 3 (X)
            processed = re.sub(pattern_add_sub, r'\1 \2 (\1*\3/100)', processed)
            # If no changes were made in this iteration, it means no more add/sub patterns exist
            if processed == original_processed:
                break

        # --- Handle remaining percentages (likely standalone or mult/div cases like 700 * 43%) ---
        # Replace X% with (X/100)
        # Note: \1 refers to capture group 1 (X)
        processed = re.sub(pattern_other, r'(\1/100)', processed)

        # print(f"Percentage Processed: {processed}") # Optional: for debugging
        return processed


    def handle_implicit_multiplication(self, expression):
        """Adds '*' for implicit multiplication cases. Called AFTER percentage processing."""
        processed = expression
        # Digit or closing parenthesis followed by opening parenthesis: 5( or )( -> add *
        processed = re.sub(r'(\d|\))(\()', r'\1*\2', processed)
         # Digit or closing parenthesis followed by function call (math., abs, etc.): 5math.( or )abs( -> add *
        processed = re.sub(r'(\d|\))(\(?(?:math|abs|pow|round)\.?\()', r'\1*\2', processed)
         # Closing parenthesis followed by digit: )5 -> add *
        processed = re.sub(r'(\))(\d)', r'\1*\2', processed)
        # Digit followed by specific math constants/functions not starting with '(': 5pi -> 5*pi
        # Be careful here not to add * between digits like 5.5
        processed = re.sub(r'(\d)(math\.(?:pi|e)\b)', r'\1*\2', processed)
        processed = re.sub(r'(\))(math\.(?:pi|e)\b)', r'\1*\2', processed)


        # print(f"Implicit Multi Processed: {processed}") # Optional: for debugging
        return processed


    # --- Core Calculation Function ---
    def calculate(self):
        """Calculates the expression in the input field."""
        try:
            expression = self.expression_input.text
            if not expression:
                self.result_label.text = ""
                return

            # --- Step 1: Preprocess Percentages ---
            # Convert percentage notations to evaluatable expressions
            processed_expression = self.preprocess_percentage(expression)

            # --- Step 2: Handle Implicit Multiplication ---
            # Add necessary '*' operators (e.g., '5(10)' -> '5*(10)')
            processed_expression = self.handle_implicit_multiplication(processed_expression)

            # --- Step 3: Evaluate the fully processed expression ---
            # Define allowed functions/globals for safety
            allowed_globals = {
                "__builtins__": {
                     'abs': abs, 'pow': pow, 'round': round,
                     'True': True, 'False': False, 'None': None,
                     'int': int, 'float': float, 'str': str,
                 },
                 "math": math # Allow access to the math module
            }
            allowed_locals = {} # No local variables needed during eval

            result = eval(processed_expression, allowed_globals, allowed_locals)

            # --- Step 4: Format result ---
            if isinstance(result, float) and result.is_integer():
                result = int(result) # Display '301' instead of '301.0'
            elif isinstance(result, float):
                 result = round(result, 10) # Limit float precision

            self.result_label.text = str(result)

        # --- Error Handling ---
        except ZeroDivisionError:
            self.result_label.text = "Error: Division by Zero"
        except OverflowError:
            self.result_label.text = "Error: Result too large"
        except SyntaxError:
             # Check if error might be related to failed preprocessing
             if '%' in expression:
                 self.result_label.text = "Error: Syntax (check % format)"
             else:
                self.result_label.text = "Error: Invalid Syntax"
        except NameError as e:
             # Handles cases where something unexpected remains after preprocessing
             self.result_label.text = f"Error: Unknown input ({e})"
        except ValueError as e:
             self.result_label.text = f"Error: Input/Value Error ({e})"
        except TypeError as e:
             # Can occur if preprocessing results in invalid operations
             self.result_label.text = f"Error: Type Mismatch ({e})"
        except Exception as e:
            # Catch any other unexpected errors
            print(f"Calculation Error Type: {type(e).__name__}, Args: {e.args}, Expression: '{expression}', Processed: '{processed_expression}'")
            self.result_label.text = "Error: Calculation Failed"

    # --- GUI Interaction Functions (remain unchanged) ---
    def add_to_expression(self, value):
        """Adds the given value to the expression input field."""
        self.expression_input.text += str(value)

    def clear_expression(self):
        """Clears the expression input and result label."""
        self.expression_input.text = ""
        self.result_label.text = ""

    def backspace(self):
        """Removes the last character from the expression input."""
        self.expression_input.text = self.expression_input.text[:-1]

# --- Kivy App Class (remains unchanged) ---
class CalculatorApp(App):
    def build(self):
        Builder.load_string(KV_STRING)
        return CalculatorLayout()

# --- Run the App (remains unchanged) ---
if __name__ == '__main__':
    # Window.size = (360, 640) # Optional
    CalculatorApp().run()
