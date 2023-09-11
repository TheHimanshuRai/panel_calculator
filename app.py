import panel as pn
pn.extension(theme = 'dark')

# Define the layout
input_box1 = pn.widgets.FloatInput(name='Input 1', value=0)
input_box2 = pn.widgets.FloatInput(name='Input 2', value=0)
output_box = pn.widgets.StaticText(name='Result', value='')

def perform_add_operation(event):
    operation = event.name
    num1 = input_box1.value
    num2 = input_box2.value
    result = num1 + num2
    output_box.value = str(result)

def perform_subtract_operation(event):
    operation = event.name
    num1 = input_box1.value
    num2 = input_box2.value
    result = num1 - num2
    output_box.value = str(result)

def perform_multiply_operation(event):
    operation = event.name
    num1 = input_box1.value
    num2 = input_box2.value
    result = num1 * num2
    output_box.value = str(result)

def perform_divide_operation(event):
    operation = event.name
    num1 = input_box1.value
    num2 = input_box2.value
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Cannot divide by zero'
    
    output_box.value = str(result)

add_button = pn.widgets.Button(name='Add', button_type='primary')
add_button.on_click(perform_add_operation)

subtract_button = pn.widgets.Button(name='Subtract', button_type='primary')
subtract_button.on_click(perform_subtract_operation)

multiply_button = pn.widgets.Button(name='Multiply', button_type='primary')
multiply_button.on_click(perform_multiply_operation)

divide_button = pn.widgets.Button(name='Divide', button_type='primary')
divide_button.on_click(perform_divide_operation)


# Inner layout to contain sll 
inner_layout = pn.Row(
    pn.Spacer(width=10),
    pn.Column(
        add_button, subtract_button, multiply_button, divide_button,
        css_classes=['operation-buttons']
    ),
    pn.Spacer(width=20),
    pn.Column(input_box1, input_box2, css_classes=['input-boxes']),
    pn.Spacer(width=20),
    pn.Column(output_box, css_classes=['output-box']),
    pn.Spacer(width=10)
)

# Using a container to apply CSS
layout = pn.Column(
    inner_layout,
    css_classes=['outer-layout']
)

# CSS for the layout
pn.config.raw_css.append('.input-boxes, .operation-buttons, .output-box, .outer-layout { border: 1px solid black; padding: 10px; }')

# Show the layout
layout.servable()
