from random import randint

from flask import Blueprint, render_template, request, session, redirect, url_for, flash, current_app, make_response, \
    jsonify

from App.SMS import sms
from App.models import *
from App.ext import db
from flask import request
from App.forms import RegisterForm
from App.verifycode import VerifyCode

bp = Blueprint('bp', __name__)


# 登陆
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        user1 = User.query.filter(User.username == username, User.password == password).first()
        user2 = User.query.filter(User.phone == username, User.password == password).first()
        if (user1 or user2):
            session['username'] = username
            return redirect('/index/')
        else:
            flash("用户名或者密码错误")
    return render_template("login.htm", **locals())


# 注册
@bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # 获取数据
            username = request.values.get('nickname')
            password = request.values.get('password')
            phone = request.values.get('phonenum')
            # 保存注册用户数据
            user = User(username=username, password=password, phone=phone)
            db.session.add(user)
            db.session.commit()
            return redirect("/")
    return render_template('regist.html', **locals())


# 文章单篇显示
@bp.route('/post/')
@bp.route("/post/<int:id>/")
def post(id=-1):
    if id < 0:
        first_art = Article.query.order_by(-Article.create_time).first()
        id = first_art.aid
    articles = db.session.query(Article, Category).filter(Article.aid == id, Article.cid == Category.cid).all()
    art_list = db.session.query(Article).filter(Article.aid == id).first()
    # 上一篇
    art_list_pre = db.session.query(Article).filter(Article.aid == (id - 1)).first()
    # 下一篇
    art_list_next = db.session.query(Article).filter(Article.aid == (id + 1)).first()
    # 最近三篇文章
    three_article = Article.query.order_by(-Article.create_time).all()[:3]
    # 所有分类
    categories = Category.query.all()
    # 分类个数
    categories_len = len(categories)
    # 标签
    tag = db.session.query(Article, Tag).filter(Article.tid == Tag.tid, Article.aid == id).first()
    tags = db.session.query(Tag).all()
    # 评论
    marks = db.session.query(Mark, User).filter(Mark.uid == User.uid).all()
    # max_mark = Mark.query().order_by(-Mark.mid).first()
    return render_template('post.html', **locals())


# 登陆后的首页
@bp.route('/index/')
def index():
    title = '时事资讯'
    articles = Article.query.all()
    category_name = Category.query.all()
    tag_name = Tag.query.all()
    return render_template('index.html', **locals())


# blog 分类显示
@bp.route('/blog/')
@bp.route('/blog/<int:cid>/')
@bp.route('/blog/<int:cid>/<int:page>/')
def bloge(cid=-1, page=1):
    if cid < 0:
        # 取默认分类的所有文章(cid=1)
        category = Category.query.first()
        cid = category.cid  # 获取第一个cid

    # 获取某一分类的所有文章
    articles = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).all()
    article_num = len(articles)

    paginate = db.session.query(Article, Category).filter(Article.cid == Category.cid, Category.cid == cid).paginate(
        page, 4)

    # 最近三篇文章
    three_article = Article.query.order_by(-Article.create_time).all()[:3]

    # 标签
    tags = Tag.query.all()

    # 分类
    categories = Category.query.all()

    return render_template('blog.html', **locals())


# 图片验证码
@bp.route('/ver/')
def ver():
    vc = VerifyCode()
    result = vc.generate()
    # 把验证码字符串存到session
    session['code'] = vc.code
    # 创建相应对象
    response = make_response(result)
    response.headers['Content-Type'] = "image/png"
    return response


# 短信验证
@bp.route("/phone_code/", methods=['GET', 'POST'])
def send_sms():
    phone = request.values.get("phonenum")
    if phone:
        # 产生验证码
        num = randint(1000, 9999)
        # 添加到session
        session['sms'] = str(num)
        para = "{'code':'%d'}" % num
        res = sms.send(phone, para)
        return res
    return render_template("regist.html")
