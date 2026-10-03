@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"❌ الخطأ: {error}")
