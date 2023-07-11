import random
from flask import Flask, request, jsonify

app = Flask(__name__)

jokes = [
    "Why did the chicken cross the playground? To get to the other slide!",
    "Why did the actor fall through the floorboards? They were going through a stage!",
    "Why did a scarecrow win a Nobel prize? He was outstanding in his field!",
    "Why are peppers the best at archery? Because they habanero!",
    "What did the duck say after she bought chapstick? Put it on my bill!",
    "Why did an old man fall in a well? Because he couldn’t see that well!",
    "What do you call a fake noodle? An impasta!",
    "What did the three-legged dog say when he walked into a saloon? I’m looking for the man who shot my paw!",
    "How do you tell the difference between a bull and a cow? It is either one or the udder!",
    "What’s red and smells like blue paint? Red paint!",
    "What’s the difference between a hippo and a Zippo? One is very heavy, the other is a little lighter!"
]

@app.route('/', methods=['GET'])
def get_joke():
    number_joke = int(request.args.get('num',1))
    if number_joke <= 0:
        return jsonify({'Invalid number of jokes defined'})

    random_joke = random.sample(jokes, number_joke)
    return jsonify({'joke of the moment': random_joke})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)