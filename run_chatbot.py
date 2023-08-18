import tkinter as tk
from PIL import ImageTk, Image
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random

# Chatbot configurations
fitness_prompts = ["How to lose weight?","What are some good exercises for getting strong?",
                   "What should we eat before a workout?", "What healthy habits should I adopt to get in better shape?",
                   "How can I improve my flexibility?", "How can I reduce stress through exercise?", "What is the best "
                                                                                                     "time to work "
                                                                                                     "out?",
                   "What are some good exercises for beginners?", "What are some common fitness injuries and how can I "
                                                                  "prevent them?",
                   "How much exercise do I need to do to stay healthy?",
                   "What is the best way to warm up before a workout?",
                   "What are the worst foods to eat for weight loss?",
                   "How do I know if I'm working out too hard?",
                   "How long should I rest between sets?",
                   "How many sets and reps should I do?",
                   "What should I eat before and after a workout?",
                   "How much water should I drink during a workout?",
                   "What are some good ways to cool down after a workout?",
                   "What are some ways to make exercise more fun?",
                   "How can I stay motivated to exercise?",
                   "What are some signs that I'm getting in shape?",
                   "What are some resources that can help me get in shape?",
                   "How can I improve my posture?",
                   "How can I improve my balance?",
                   "How can I increase my endurance?",
                   "What are some ways to get help with eating healthy?",
                   "What are some tips for avoiding unhealthy food cravings?",
                   "What are some tips for eating healthy on a budget?",
                   "What are the best foods to eat for muscle gain?",
                   "What are the worst foods to eat for weight loss?",
                   "What are the best snacks to eat throughout the day?",
                   "What are some tips for making healthy changes to your diet?",
                   "What are some healthy and affordable food options?",
                   "What are some tips for cooking healthy meals at home?",
                   "Is candy healthy?", "What are some healthy food?",
                   "What is a good diet?", "How to stay fit?",
                   "How does cardio fitness contribute to strength training?",
                   "How can goal setting help with weight management?", "Why are vitamins and minerals important in"
                                                                        "meal planning?",
                   "How can strength training help prevent injuries?", "What are macronutrients and why are they "
                                                                       "important in meal planning?",
                   "What are some essential fitness gear and equipment for home workouts?", "Is spot reduction "
                                                                                            "possible for losing fat "
                                                                                            "in specific body areas?",
                   "What are the benefits of strength training?", "What are some tips for staying motivated to "
                                                                  "exercise?",
                   "What are some common fitness myths?", "What are some good sports for beginners?",
                   "What are some healthy snacks for athletes?", "What are some common injuries that athletes can "
                                                                 "experience?",
                   "What are some benefits of stretching?", "What are some tips for choosing the right fitness gear?",
                   "What are some healthy meal options for people who are trying to lose weight?", "What are some "
                                                                                                   "tips for staying "
                                                                                                   "hydrated while "
                                                                                                   "exercising?",
                   "What are some resources for finding a fitness buddy?", "How does sports improve cardiovascular "
                                                                           "health?",
                   "How does sports improve bone health?", "How does sports improve muscle health?", "How does sports "
                                                                                                     "improve mental "
                                                                                                     "health?"]
fitness_responses = [
    "You can try incorporating more cardiovascular exercises into your routine and reducing your calorie intake.", "Weightlifting and body weight exercises like push-ups and pull-ups are great for building muscle.",
    "Eating a balanced meal with carbs and protein 1-2 hours before a workout\n can provide you with energy and fuel "
    "your muscles.",
    "Yoga and stretching exercises like Pilates and barre can help improve your flexibility.",
    "Exercise releases endorphins which can help reduce stress. Try incorporating activities like walking or swimming "
    "into your routine.",
    "The best time to work out is when you are most likely to stick to your routine. It is important to find a time "
    "that works for "
    "you and your schedule.", "Some popular options include walking, "
                              "jogging, swimming, and biking. It is important to find exercises\n that you enjoy and "
                              "that are appropriate for your fitness level.", "The common fitness "
                                                                              "injuries are muscle strains, "
                                                                              "ligament sprains, and overuse injuries. "
                                                                              "These injuries can be prevented by "
                                                                              "warming up before exercise, cooling "
                                                                              "and using proper form.",
    "Aim for at least 30 minutes of moderate-intensity exercise most days of the week.",
    "Do a light cardio workout for 5-10 minutes, followed by some dynamic stretches.",
    "Processed foods, sugary drinks, and unhealthy fats.",
    "If you're feeling pain, you're probably working out too hard.",
    "Rest for 1-2 minutes between sets.",
    "Aim for 3 sets of 8-12 reps for each exercise.",
    "Eat a healthy snack before a workout and a balanced meal after a workout.",
    "Drink 1-2 cups of water every 15-20 minutes during a workout.",
    "You should Stretch, walk, or do some light cardio before workout.",
    "Listen to music, try new activities, exercise with friends.",
    "Set realistic goals, track your progress, reward yourself.",
    "I have more energy, I sleep better, I'm losing weight.",
    "Some signs that you are getting in shape may include: 1. You have more energy"
    "2. You sleep better 3. You have less aches and pains",
    "Personal trainers, fitness classes, online resources.",
    "Strengthening your core muscles and practicing good posture habits.",
    "Balance exercises like yoga or standing on one leg.",
    "Cardiovascular exercise and interval training.",
    "Talk to your doctor, a registered dietitian, or a certified personal trainer.",
    "Eat regular meals and snacks, get enough sleep, and manage stress.",
    "Buy in bulk, cook at home, and shop at discount stores.",
    "Whole, unprocessed foods, such as lean protein, complex carbohydrates, and healthy fats.",
    " Processed foods, sugary drinks, and unhealthy fats.",
    "Fruits,nuts and vegetables.",
    "Start small, make gradual changes, and don't give up.",
    "Fruits, vegetables, whole grains, lean protein, and healthy fats.",
    "You can use fresh ingredients, limit processed foods, and cook in healthy oils.",
    "No it is not good for your health.",
    "Some healthy food to stay fit include red meat, pulses, green vegetables, etc.",
    "A good diet varies is a balanced intake of calories.",
    "You can stay healthy by eating good and doing exercise.", "Cardio fitness improves endurance, helps burn "
                                                               "calories, and supports overall cardiovascular health, "
                                                               "enhancing performance during strength training "
                                                               "exercises.",
    "Setting specific and achievable goals, such as losing a certain amount of weight or exercising for a set\n "
    "duration, provides motivation and a sense of progress in weight management journeys.",
    "Vitamins and minerals play essential roles in maintaining overall health, supporting bodily functions,\n "
    "boosting the immune system, and preventing nutrient deficiencies.",
    "Strength training improves muscular strength, stability, and flexibility, reducing the risk of injuries.",
    "Macronutrients, including carbohydrates, proteins, and fats, are essential nutrients needed in large quantities\n "
    "for energy, growth, and bodily functions.",
    "Some essential fitness gear and equipment for home workouts include resistance bands, dumbbells or kettle bells,"
    "\n "
    "exercise mat offering versatility and effectiveness in training routines.",
    "No, spot reduction is a myth; fat loss occurs throughout the body as a whole, and targeted exercises can\n "
    "strengthen and tone specific muscles.",
    "Strength training can help you build muscle, lose weight, and improve your overall health.",
    "Some tips for staying motivated to exercise include finding an activity you enjoy, setting realistic goals,\n"
    "and working out with a friend.",
    "Some common fitness myths include that you need to do a lot of cardio to lose weight, that you can spot reduce\n"
    "fat, and that you can't build muscle without using weights.",
    "Some good sports for beginners include walking, jogging, swimming, and biking.\n These sports are low-impact and "
    "easy, making them a good option for people who are new to exercise.",
    "Some healthy snacks for athletes include fruits, vegetables, nuts, and yogurt. These snacks are a good source of\n"
    "energy and nutrients, and they can help to refuel the body after a workout.",
    "Some common injuries that athletes can experience include sprains, strains, fractures, concussions,\n"
    "and tendinitis, which can occur due to overuse, impact, or sudden movements during sports activities. Proper\n "
    "warm-up, conditioning, and technique can help reduce the risk of these injuries.",
    "Stretching can help to improve flexibility, reduce muscle soreness, and prevent injuries.",
    "When choosing fitness gear, it is important to consider your fitness goals, your body type, and your budget.",
    "Some healthy meal options for people who are trying to lose weight include lean protein, whole grains, fruits,\n"
    "and vegetables.",
    "It is important to drink plenty of fluids before, during, and after exercise. Water is the best choice, "
    "but you can also drink sports drinks if you need extra electrolytes.",
    "There are many resources available for finding a fitness buddy. You can ask friends, family, or co-workers if \n"
    "they are interested in working out with you.",
    "Sports can improve cardiovascular health by increasing heart rate and blood flow. This can help to lower blood \n"
    "pressure, reduce the risk of heart disease, and improve overall cardiovascular health.",
    "Sports can improve bone health by putting stress on the bones. This stress helps to stimulate bone growth and "
    "development.",
    "Sports can improve muscle health by increasing muscle mass and strength. This can help to improve physical "
    "performance and reduce the risk of injuries.",
    "Sports can improve mental health by reducing stress, anxiety, and depression. Sports can also help to improve\n "
    "self-esteem and confidence."
    "I'm sorry, I could not understand. Could you please provide more information about your health inquiry?"
]
bot_name = "Fitness Bot"

# Function to generate a random response
def get_random_response(responses):
    return random.choice(responses)

# Function to get the best matching question
def get_best_match(question, choices):
    return process.extractOne(question, choices)[0]

# Function to handle the user's input
def handle_user_input():
    # Get the user's input
    user_input = user_input_box.get()
    # If the user wants to exit, close the GUI
    if user_input.lower() == "exit" or user_input.lower() == "quit":
        print("Thanks for having a conversation with me. Goodbye!")
        root.destroy()
    else:
        # Get the best matching question
        best_question_match = get_best_match(user_input, fitness_prompts)
        similarity_ratio = fuzz.ratio(user_input.lower(), best_question_match.lower())

        if similarity_ratio >= 50:  # Adjust the similarity threshold as per your requirements
            index = fitness_prompts.index(best_question_match)
            response = fitness_responses[index]
        else:
            response = get_random_response(fitness_responses)

        # Update the response label with the chatbot response
        prompt_history.config(text=f"You: {user_input}")
        prompt_history.pack()

        chat_history.config(text=f"{bot_name}: {response}")
        chat_history.pack()


# Create the main window
root = tk.Tk()
root.title("Health and Fitness Chatbot")
root.geometry("1350x950")

# Set the background image
background_image = Image.open("Place the address of the picture in your laptop")
background_image = background_image.resize((1350,950))
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Load the logo image and resize it
logo_image = Image.open("Place the address of the picture in your laptop")
logo_image = logo_image.resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label for the logo image and display it
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack()

# Create the chatbot label
chatbot_label = tk.Label(root,
                         text=f"{bot_name}: Hello! I'm your health and fitness chatbot. How can I help you today?",
                         font=("Arial", 16))
chatbot_label.pack()

# Create the user input box
user_input_box = tk.Entry(root, width=50, font=("Arial", 14))
user_input_box.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", background='light blue', command=handle_user_input, height=2, padx=5,
                          pady=5, font=("Arial", 11))
submit_button.pack()

# Prompt history
prompt_history = tk.Label(root, text="", width=100, height=1, font=("Times New Roman", 14))
prompt_history.pack()

# Chat history
chat_history = tk.Label(root, text="", width=100, height=4, font=("Times New Roman", 14))
chat_history.pack()

# Create labels for the height and weight input boxes.
height_label = tk.Label(root, text="Height (in cm):", height=1)
height_label.pack()

# Create text boxes for the height and weight input boxes.
height_entry = tk.Entry(root, width=50, font=("Arial", 14))
height_entry.pack()

weight_label = tk.Label(root, text="Weight (in kg):", height=1)
weight_label.pack()

weight_entry = tk.Entry(root, width=50, font=("Arial", 14))
weight_entry.pack()

# Calculate the BMI and display it in a label.
def calculate_BMI():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = round(weight / (height / 100) ** 2,2)
    label.config(text=f"BMI is: " + str(bmi))
    label.pack()
    # Classify the BMI
    if bmi <= 18.5:
        label1.config(text=f"You are underweight.")
        label1.pack()
    elif bmi <= 24.9:
        label1.config(text=f"You are healthy.")
        label1.pack()
    elif bmi <= 29.9:
        label1.config(text=f"You are overweight.")
        label1.pack()
    elif bmi <= 34.9:
        label1.config(text=f"You are obese.")
        label1.pack()
    else:
        label1.config(text=f"You are severely obese.")
        label1.pack()

# Create a frame for the BMI section
bmi_frame = tk.Frame(root)
bmi_frame.pack()

# Create a button that will calculate the BMI.
calculate_button = tk.Button(bmi_frame, text="Calculate your BMI", background='light blue', command=calculate_BMI, height=2,
                             width=15, padx=5, pady=5, font=("Arial", 11))
calculate_button.pack()

label = tk.Label(bmi_frame, text="", width=20, height=1, font=("Times New Roman", 14))
label.pack(side=tk.LEFT)

label1 = tk.Label(root, text="", width=100, height=1, font=("Times New Roman", 14))
label1.pack()

root.mainloop()
