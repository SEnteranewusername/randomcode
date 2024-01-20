from dtmf import generate
import dtmf.model as model

obj = model.String([
    model.Tone("3"),
    model.Tone("1"),
    model.Tone("3"),
    model.Tone("2"),
    model.Tone("3"),
    model.Tone("1"),
    model.Tone("1"),
    model.Pause(),
    model.Tone("1"),
    model.Tone("3"),
    model.Tone("3"),
    model.Tone("#")
])

audio = generate(obj)