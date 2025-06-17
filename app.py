from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime
from datetime import timedelta
from collections import defaultdict

app = Flask(__name__)

DATA_FILE = 'data.json'

# 初期化: data.json がなければ空の構造を作成
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({"skills": [], "logs": []}, f, indent=2, ensure_ascii=False)

def load_data():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    logs = data.get('logs', [])
    # IDがなければ付ける
    changed = False  # IDを付けたかどうかのフラグ
    for i, log in enumerate(logs, start=1):
        if 'id' not in log:
            log['id'] = i
            changed = True
    # もしIDを追加したらファイルを更新
    if changed:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    return data

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/')
def index():
    data = load_data()
    today_logs = [log for log in data['logs'] if log['date'] == datetime.today().strftime('%Y-%m-%d')]
    total_time = sum(int(log['time']) for log in today_logs)
    return render_template('index.html', total_time=total_time, today_logs=today_logs)

@app.route('/skills', methods=['GET', 'POST'])
def skills():
    data = load_data()
    if request.method == 'POST':
        name = request.form['name']
        time = int(request.form['time'])
        data['skills'].append({"name": name, "time": time})
        save_data(data)
        return redirect('/skills')
    return render_template('skills.html', skills=data['skills'])

@app.route('/log', methods=['GET', 'POST'])
def log():
    data = load_data()
    if request.method == 'POST':
        title = request.form['title']
        skill = request.form['skill']
        time = request.form['time']
        memo = request.form['memo']
        date = datetime.today().strftime('%Y-%m-%d')
        data['logs'].append({
            "title": title,
            "skill": skill,
            "time": time,
            "memo": memo,
            "date": date
        })
        save_data(data)
        return redirect('/log')
    return render_template('log.html', logs=data['logs'])

@app.route('/graph')
def graph():
    data = load_data()
    logs = data['logs']

    # 直近7日間の日付と勉強時間を集計
    daily_totals = defaultdict(int)
    today = datetime.today()

    for i in range(7):
        date_str = (today - timedelta(days=i)).strftime('%Y-%m-%d')
        daily_totals[date_str] = 0

    for log in logs:
        if log['date'] in daily_totals:
            daily_totals[log['date']] += int(log['time'])

    # 日付順に整える
    dates = sorted(daily_totals.keys())
    totals = [daily_totals[date] for date in dates]

    return render_template('graph.html', dates=dates, totals=totals)

@app.route('/manage')
def manage():
    data = load_data()
    logs = data.get('logs', [])
    return render_template('manage.html', logs=logs)

@app.route('/edit/<int:log_id>', methods=['GET', 'POST'])
def edit(log_id):
    data = load_data()
    logs = data.get('logs', [])
    log = next((l for l in logs if l['id'] == log_id), None)
    if not log:
        return "指定されたログが見つかりません。", 404

    if request.method == 'POST':
        log['title'] = request.form['title']
        log['time'] = request.form['time']
        log['memo'] = request.form['memo']
        log['date'] = request.form['date']
        save_data(data)
        return redirect('/manage')

    return render_template('edit.html', log=log)

@app.route('/delete/<int:log_id>', methods=['POST'])
def delete(log_id):
    data = load_data()
    logs = data.get('logs', [])
    new_logs = [log for log in logs if log['id'] != log_id]
    data['logs'] = new_logs
    save_data(data)
    return redirect('/manage')

if __name__ == '__main__':
    app.run(debug=True)
