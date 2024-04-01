document.getElementById('startLesson').addEventListener('click', function() {
    document.getElementById('menu').style.display = 'none';
    document.getElementById('lesson').style.display = 'block';
});

const punctuations = document.querySelectorAll('.punctuation');
punctuations.forEach(punc => {
    punc.addEventListener('dragstart', dragStart);
});

function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.textContent);
}

document.getElementById('sentence').addEventListener('click', function(e) {
    if (e.target.classList.contains('punctuation-placeholder')) {
        e.target.textContent = '';
        e.target.contentEditable = true;
        e.target.focus();
    }
});

document.getElementById('checkAnswer').addEventListener('click', function() {
    // This is where you'd check the answer.
    // For simplicity, let's just log the content for now.
    console.log(document.getElementById('sentence').textContent);
    // You would check the answer here and then show "Next Question" or "Incorrect Answer"
});
