@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ ما عندك صلاحية تستخدم هالأمر.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("❌ البوت ما عنده الصلاحية المطلوبة.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ لازم تحدد الشخص، مثال: !kick @الشخص")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("❌ ما قدرت ألقى هذا العضو.")
    else:
        await ctx.send(f"❌ صار خطأ: `{error}`")
