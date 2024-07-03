import csv
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Read sentiment scores from CSV file
def run(bank):
    sentiment_scores = []
    with open(f"{bank}_sentiments.csv", "r", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentiment_scores.append(float(row["Description_Sentiment"]))

    # Calculate average sentiment score
    average_score = sum(sentiment_scores) / len(sentiment_scores)

    # Define sentiment categories and corresponding colors
    sentiment_categories = ["Strong Sell", "Sell", "Neutral", "Buy", "Strong Buy"]
    sentiment_colors = ["red", "orange", "yellow", "limegreen", "green"]

    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(8, 4))

    # Create a filled semicircular dial
    dial = patches.Arc((0, 0), width=2, height=1, angle=0, theta1=0, theta2=180, linewidth=3, edgecolor='black', facecolor='lightgray')
    ax.add_patch(dial)

    # Fill the semicircular shape with colors
    for i, color in enumerate(sentiment_colors):
        start_angle = i * (180 / (len(sentiment_categories)))
        end_angle = (i + 1) * (180 / (len(sentiment_categories)))
        wedge = patches.Wedge((0, 0), 1, start_angle, end_angle, edgecolor='black', facecolor=color)
        ax.add_patch(wedge)

    # Add ticks for sentiment categories
    for i, category in enumerate(sentiment_categories):
        angle = i * (180 / (len(sentiment_categories) - 1))
        x = math.cos(math.radians(angle)) * 0.9
        y = math.sin(math.radians(angle)) * 0.9
        ax.text(x, y, category, ha='center', va='center', fontsize=12, color='black')

    # Calculate the angle for the needle
    angle = (average_score / 1) * 180

    # Draw the black needle
    needle = patches.Arrow(0, 0, math.cos(math.radians(angle)), math.sin(math.radians(angle)),
                        width=0.05, color='black', edgecolor='black')
    ax.add_patch(needle)

    # Set axis limits and aspect ratio
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.set_aspect('equal', adjustable='box')

    # Show axes
    ax.axis('off')

    # Set title and increase font size
    ax.set_title('Sentiment Analysis Gauge', fontsize=16)

    # Show the plot
    plt.savefig(f'SG.{bank}.NS.png', dpi=300, bbox_inches='tight')




run('IDFC')
run('INDUSIND')
run('KOTAK')
run('PNB')
run('SBI')
run('ICICI')
