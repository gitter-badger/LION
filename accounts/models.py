from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import os, random, string

# Create your models here.

def get_image_path(instance, filename):
    
    return os.path.join(
        'idcard', 
        str(instance.username),
        filename
    )

class User(AbstractUser):

    def __str__(self):
        activator_str = self.last_name + " " + self.first_name
        return activator_str

    id_valid = RegexValidator(regex=(r'^[0-9]{10}$'), message=("学生番号はハイフンなしの半角数字10桁で入力してください！"))
    tel_valid = RegexValidator(regex=(r'^[0-9]+$'), message=("電話番号はハイフンなしの半角数字で入力してください！"))

    username = models.CharField(
        validators=[id_valid],
        max_length=10,
        verbose_name='学生番号',
        unique=True
    )

    email = models.EmailField(
        verbose_name='Eメールアドレス'
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name='姓'
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name='名'
    )    

    kana_valid = RegexValidator(regex=(r'^[ぁ-んー]+$'), message=("ひらがなで入力してください！"))

    last_name_kana = models.CharField(
        validators=[kana_valid],
        max_length=100,
        verbose_name='姓（かな）'
    )

    first_name_kana = models.CharField(
        validators=[kana_valid],
        max_length=100,
        verbose_name='名（かな）'
    )    

    telephone = models.CharField(
        validators=[tel_valid],
        max_length=15,
        verbose_name='電話番号（ハイフンなし）'
    )

    sougou = '総人'
    bungaku = '文学'
    kyouiku = '教育'
    hougaku = '法学'
    keizai = '経済'
    rigaku = '理学'
    kougaku = '工学'
    nougaku = '農学'
    igaku = '医学'
    yakugaku = '薬学'
    sonota = '他'

    FACULTY = (
        (sougou, '総合人間学部 / 人間・環境学研究科'),
        (bungaku, '文学部 / 文学研究科'),
        (kyouiku, '教育学部 / 教育学研究科'),
        (hougaku, '法学部 / 法学研究科'),
        (keizai, '経済学部 / 経済研究科'),
        (rigaku, '理学部 / 理学研究科'),
        (kougaku, '工学部 / 工学研究科 / 情報学研究科'),
        (nougaku, '農学部 / 農学研究科'),
        (igaku, '医学部 / 医学研究科'),
        (yakugaku, '薬学部 / 薬学研究科'),
        (sonota, 'その他学部 / 大学院等')
    )    

    faculty = models.CharField(
        max_length=10,
        choices=FACULTY,
        verbose_name='所属'
    )

    B1 = 'B1'
    B2 = 'B2'
    B3 = 'B3'
    B4 = 'B4'
    B5 = 'B5'
    B6 = 'B6'
    MR = '修士'
    DR = '博士'
    OT = '他'

    GRADE = (
        (B1, '学部1回生'),
        (B2, '学部2回生'),
        (B3, '学部3回生'),
        (B4, '学部4回生'),
        (B5, '学部5回生'),
        (B6, '学部6回生以上'),
        (MR, '修士課程'),
        (DR, '博士課程'),
        (OT, 'その他')
    )
    grade = models.CharField(
        max_length=2,
        choices=GRADE,
        verbose_name='回生')

    idcard = models.ImageField(
        upload_to=get_image_path,
        verbose_name="学生証画像"
    )


class Project(models.Model):
    activator = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name="activator"
    )

    leader = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name="leader"
    )

    member = models.ManyToManyField(
        'User',
        related_name="member"
    )

    name = models.CharField(
        max_length = 100,
        verbose_name = "団体名"
    )

    name_kana = models.CharField(
        max_length = 100,
        verbose_name = "団体名（かな）"
    )

    activation_no = models.CharField(
        max_length = 6,
        verbose_name = "申請書コード",
        help_text="半角英字で入力してください。例：「xM-001」"
    )

    mogi = '模擬'
    ground ='グラ'
    okunai = '屋内'
    stage = 'ステ'
    jise = '演劇'

    KIND=(
        (mogi, '模擬店企画'),
        (ground, 'グラウンド企画'),
        (okunai, '屋内企画'),
        (stage, 'ステージ企画'),
        (jise, '自主制作演劇企画')
    )

    kind = models.CharField(
        max_length = 10,
        verbose_name = "企画種別",
        choices=KIND
    )