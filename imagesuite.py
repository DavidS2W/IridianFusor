import requests
from discord.ext import commands
import discord
from PIL import Image, ImageEnhance
from io import BytesIO

async def flip_img(ctx, reply_msg, arg2):
  try:
    atch = reply_msg.attachments[0]
    response  = requests.get(atch.url)
    img_pil = Image.open(BytesIO(response.content))
    if str(arg2).lower() != 'vertical' or arg2 ==None:
      img_edited = img_pil.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    else:
      img_edited = img_pil.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)


    with BytesIO() as image_binary:
      img_edited.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.reply(f'Flipped {atch.filename}')
      await ctx.send(file=discord.File(fp=image_binary, filename=f'{atch.filename}'))
  except:
    response  = requests.get(reply_msg.content)
    img_pil = Image.open(BytesIO(response.content))
    if str(arg2).lower() != 'vertical' or arg2 ==None:
      img_edited = img_pil.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    else:
      img_edited = img_pil.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)


    with BytesIO() as image_binary:
      img_edited.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.reply(f'Flipped {reply_msg.content}')
      await ctx.send(file=discord.File(fp=image_binary, filename=f'{reply_msg.content}.png'))

async def resize_img(ctx, reply_msg, arg1, arg2):
  if len(reply_msg.attachments) == 0:
    response = requests.get(reply_msg.content)
    filea = reply_msg.content
  else:
    response = requests.get(reply_msg.attachments[0].url)
    filea = reply_msg.attachments[0].filename

  img_pil = Image.open(BytesIO(response.content))
  ori_size = img_pil.size
  
  img_edited = img_pil.resize(size=(int(arg1), int(arg2)))


  with BytesIO() as image_binary:
    
      img_edited.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.reply(f'Resized {filea} to `{arg1}x{arg2}` from `{ori_size[0]}x{ori_size[1]}`')
      await ctx.send(file=discord.File(fp=image_binary, filename=f'{filea}'))


async def sharpen_img(ctx, reply_msg, arg1):
  if len(reply_msg.attachments) == 0:
    response = requests.get(reply_msg.content)
    filea = reply_msg.content
  else:
    response = requests.get(reply_msg.attachments[0].url)
    filea = reply_msg.attachments[0].filename

  img_pil = Image.open(BytesIO(response.content))
  
  sharpener = ImageEnhance.Sharpness(img_pil)
  img_edited = sharpener.enhance(int(arg1)/5)

  with BytesIO() as image_binary:
    
    img_edited.save(image_binary, 'PNG')
    image_binary.seek(0)
    if int(arg1) > 1:
      await ctx.reply(f'Sharpened {filea} by {int(arg1)}%')
    else:
      await ctx.reply(f'Sharpened {filea} by {int(arg1)}%')
    await ctx.send(file=discord.File(fp=image_binary, filename=f'{filea}'))

async def contrast_img(ctx, reply_msg, arg1):
  if len(reply_msg.attachments) == 0:
    response = requests.get(reply_msg.content)
    filea = reply_msg.content
  else:
    response = requests.get(reply_msg.attachments[0].url)
    filea = reply_msg.attachments[0].filename

  img_pil = Image.open(BytesIO(response.content))
  
  sharpener = ImageEnhance.Contrast(img_pil)
  img_edited = sharpener.enhance(int(arg1)/10)

  with BytesIO() as image_binary:
    
    img_edited.save(image_binary, 'PNG')
    image_binary.seek(0)
    if int(arg1) > 1:
      await ctx.reply(f'Changed the contrast of {filea} by {int(arg1)}%')
    else:
      await ctx.reply(f'Changed the contrast of {filea} by {int(arg1)}%')
    await ctx.send(file=discord.File(fp=image_binary, filename=f'{filea}'))

async def all_things_bright_and_beautiful(ctx, reply_msg, arg1):
  if len(reply_msg.attachments) == 0:
    response = requests.get(reply_msg.content)
    filea = reply_msg.content
  else:
    response = requests.get(reply_msg.attachments[0].url)
    filea = reply_msg.attachments[0].filename

  img_pil = Image.open(BytesIO(response.content))
  
  sharpener = ImageEnhance.Brightness(img_pil)
  if int(arg1) < 0:
    num = (100 + int(arg1))/100
    img_edited = sharpener.enhance(num)
  else:
    img_edited = sharpener.enhance(int(arg1)/10)
    

  with BytesIO() as image_binary:
    
    img_edited.save(image_binary, 'PNG')
    image_binary.seek(0)
    if int(arg1) > 1:
      await ctx.reply(f'Changed the brightness of {filea} by {int(arg1)}%')
    else:
      await ctx.reply(f'Changed the brightness of {filea} by {int(arg1)}%')
    await ctx.send(file=discord.File(fp=image_binary, filename=f'{filea}'))


async def rotate_image(ctx, reply_msg, arg2):
  try:
    atch = reply_msg.attachments[0]
    print(atch)
    response  = requests.get(atch.url)
    img_pil = Image.open(BytesIO(response.content))
    img_edited = img_pil.rotate(int(arg2), expand=1)


    with BytesIO() as image_binary:
      img_edited.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.reply(f'Rotated {atch.filename} by {arg2}°')
      await ctx.send(file=discord.File(fp=image_binary, filename=f'{atch.filename}'))
  except:
    response  = requests.get(reply_msg.content)
    img_pil = Image.open(BytesIO(response.content))
    img_edited = img_pil.rotate(int(arg2))


    with BytesIO() as image_binary:
      img_edited.save(image_binary, 'PNG')
      image_binary.seek(0)
      await ctx.reply(f'Rotated {reply_msg.content} by {arg2}°')
      await ctx.send(file=discord.File(fp=image_binary, filename=f'{reply_msg.content}.png'))
