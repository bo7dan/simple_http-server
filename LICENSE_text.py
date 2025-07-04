import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

root.title("License")

root.geometry("800x600")

text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 10))
text_area.pack(expand=True, fill='both')

license_text = """\
                      GNU GENERAL PUBLIC LICENSE
                         Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

 The GNU General Public License is a free, copyleft license for
 software and other kinds of works.

 The licenses for most software and other practical works are designed to
 take away your freedom to share and change the works. By contrast,
 the GNU General Public License is intended to guarantee your freedom to
 share and change all versions of a program--to make sure it remains free
 software for all its users. We, the Free Software Foundation, use the
 GNU General Public License for most of our software; it applies also to
 any other work released this way by its authors. You can apply it to
 your programs, too.

 When we speak of free software, we are referring to freedom, not price.
 Our General Public Licenses are designed to make sure that you have the
 freedom to distribute copies of free software (and charge for them if you wish),
 that you receive source code or can get it if you want it, that you can change
 the software or use pieces of it in new free programs, and that you know you
 can do these things.

 To protect your rights, we need to prevent others from denying you these
 rights or asking you to surrender the rights. Therefore, you have certain
 responsibilities if you distribute copies of the software, or if you modify it:
 responsibilities to respect the freedom of others.

 For example, if you distribute copies of such a program, whether gratis or
 for a fee, you must pass on to the recipients the same freedoms that you
 received. You must make sure that they, too, receive or can get the source
 code. And you must show them these terms so they know their rights.

 Developers that use the GNU GPL protect your rights with two steps:
 (1) assert copyright on the software, and (2) offer you this License
 giving you legal permission to copy, distribute and/or modify it.

 For the developers' and authors' protection, the GPL clearly explains that
 there is no warranty for this free software. For both users' and authors'
 sake, the GPL requires that modified versions be marked as such, so that
 their problems will not be attributed erroneously to authors of previous
 versions.

 Some devices are designed to deny users access to install or run modified
 versions of the software inside them, although the manufacturer can do so.
 This is fundamentally incompatible with the aim of protecting users' freedom
 to change the software. Thus, we have designed this version of the GPL to
 prohibit such practices for products where the user's right to change and
 install modified versions of the software is paramount.

 We invite you to check out how this License, in the "Conditions" section
 below, protects the users' freedoms.

                        TERMS AND CONDITIONS

 0. Definitions.

 "This License" refers to version 3 of the GNU General Public License.

 "The Program" refers to any copyrightable work licensed under this License.
 Each licensee is addressed as "you". "Licensees" and "recipients" may be
 individuals or organizations.

 To "modify" a work means to copy from or adapt all or part of the work in a
 fashion requiring copyright permission, other than the making of an exact
 copy. The resulting work is called a "modified version" of the earlier work
 or a work "based on" the earlier work.

 A "covered work" means either the unmodified Program or a work based on the Program.

 To "propagate" a work means to do anything with it that, without permission,
 would make you directly or secondarily liable for infringement under
 applicable copyright law, except executing it on a computer or modifying a
 private copy. Propagation includes copying, distribution (with or without
 modification), making available to the public, and in some countries other
 activities as well.

 To "convey" a work means any kind of propagation that enables other parties to make
 or receive copies. Mere interaction with a user through a computer network,
 with no transfer of a copy, is not conveying.

 An interactive user interface displays "Appropriate Legal Notices" to the
 extent that it includes a convenient and prominently visible feature that
 (1) displays an appropriate copyright notice, and (2) tells the user that there
 is no warranty for the work (provided that the users are not otherwise
 supplied with a warranty) and that licensees may convey the work under this
 License, and how to view a copy of this License. If the interface presents
 a list of user commands or options, such as a menu, a prominent item in the
 list would suffice.

 1. Source Code.

 The "source code" for a work means the preferred form of the work for making
 modifications to it. "Object code" means any non-source form of a work.

 A "Standard Interface" means an interface that either is an official standard
 defined by a recognized standards body, or, in the case of computer programs,
 an interface customarily used by developers working in that language.

 The "System Libraries" of an executable work include anything, other than the
 work as a whole, that (a) is included in the normal form of packaging a
 Major Component, but which is not part of that Major Component, and (b)
 serves only to enable use of the work with that Major Component, or to
 implement a Standard Interface for which an implementation is available to
 the public in source code form. A "Major Component", in this context, means
 a major essential component (kernel, window system, and so on) of the
 specific operating system (if any) on which the executable work runs, or a
 compiler used to produce the work, or an interpreter used to run it.

 The "Corresponding Source" for a work in object code form means all the
 source code needed to generate, install, and run the object code and to
 modify the work, including scripts to control those activities. However, it
 does not include the work's System Libraries, or general-purpose tools or
 generally available free programs which are used unmodified in performing
 those activities but which are not part of the work. For example,
 Corresponding Source includes interface definition files associated with
 source files, and the source code for shared libraries and dynamically
 linked subprograms that the work is specifically designed to require,
 such as by intimate data communication or control flow between those
 subprograms and other parts of the work.

 The Corresponding Source need not include anything that users can regenerate
 automatically from other parts of the Corresponding Source.

 The Corresponding Source for a work in object code form is a "Complete
 Corresponding Source" if it includes all the source code for all modules it
 contains, plus any associated interface definition files, plus the scripts
 used to control compilation and installation of the executable.

 2. Basic Permissions.

 All rights granted under this License are granted for the term of copyright
 on the Program, and are irrevocable provided the stated conditions are met.
 This License explicitly affirms your unlimited permission to run the
 unmodified Program. The output from running a covered work is covered by this
 License only if the output, given its content, constitutes a covered work.
 This License acknowledges your rights of fair use or other equivalent, as
 provided by copyright law.

 You may make, run and propagate covered works that you do not convey, without
 condition so long as your license otherwise remains in force. You may convey
 covered works to others for the sole purpose of having them make modifications
 exclusively for you, or provide you with facilities for running those works,
 provided that you comply with the terms of this License in conveying all
 material for which you do not control copyright. Those thus made or run for
 you must be treated as production of a covered work by you for all purposes of
 this License.

 3. Protecting Users' Legal Rights From Anti-Circumvention Law.

 No covered work shall be deemed part of an effective technological measure
 under any applicable law fulfilling obligations under Article 11 of the WIPO
 Copyright Treaty adopted on 20 December 1996, or similar laws prohibiting or
 restricting circumvention of technological measures.

 When you convey a covered work, you waive any legal power to forbid
 circumvention of technological measures to the extent such circumvention is
 effected by exercising rights under this License with respect to the covered
 work, and you disclaim any intention to limit operation or modification of
 the work to the extent that it is a means of exercising rights under this
 License.

 4. Conveying Verbatim Copies.

 You may convey verbatim copies of the Program's source code as you receive it,
 in any medium, provided that you conspicuously and appropriately publish on
 each copy an appropriate copyright notice; keep intact all notices stating
 that this License and any non-permissive terms added in accord with section 7
 apply to the code; keep intact all notices of the absence of any warranty;
 and give all recipients a copy of this License along with the Program.

 You may charge any price or no price for each copy that you convey, and you may
 offer support or warranty protection for a fee.

 5. Conveying Modified Source Versions.

 You may convey a work based on the Program, or the modifications to produce it
 from the Program, in the form of source code under the terms of section 4,
 provided that you also meet all of these conditions:

 a) The work must carry prominent notices stating that you modified it, and
    giving a relevant date.
 b) The work must carry prominent notices stating that it is released under this
    License and any conditions added under section 7. This requirement modifies
    the requirement in section 4 to "keep intact all notices".
 c) You must license the entire work, as a whole, under this License to anyone
    who comes into possession of a copy. This License will therefore apply, along
    with any applicable section 7 additional terms, to the whole of the work,
    and all its parts, regardless of how they are packaged. This License gives
    no permission to license the work in any other way, but it does not invalidate
    such permission if you have separately received it.
 d) If the work has interactive user interfaces, each must display
    "Appropriate Legal Notices"; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your work
    need not make them do so.

 A compilation of a covered work with other separate and independent works,
 which are not by their nature extensions of the covered work, and which are
 not combined with it such as to form a larger program, in or on a volume of
 a storage or distribution medium, is called an "aggregate". An aggregate does
 not require this License to apply to the other parts of the aggregate.

 6. Conveying Non-Source Forms.

 You may convey a covered work in object code form under the terms of sections
 4 and 5, provided that you also meet all of these conditions:

 a) Convey the object code in, or embodied in, a physical product (including
    a physical distribution medium), or in a medium customarily used for
    software interchange.
 b) Convey the Corresponding Source in a physical product (including a physical
    distribution medium) or in a medium customarily used for software
    interchange, along with the object code, or with a written offer, valid
    for at least three years and valid for as long as you offer spare parts
    or customer support for that product model, to give anyone who possesses
    the object code either (1) a copy of the Corresponding Source for all
    the software in the product that is covered by this License, on a durable
    physical medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this conveying of
    source, or (2) access to copy the Corresponding Source from a network server
    at no charge.
 c) Convey to the user an copy of this License.

 A "User Product" is either (1) a "consumer product", which means any tangible
 personal property which is normally used for personal, family, or household
 purposes, or (2) anything designed or sold for incorporation into a dwelling.
 In determining whether a product is a consumer product, doubtful cases shall
 be resolved in favor of coverage. For a particular product received by a
 particular user, "normally used" refers to a typical or common use of that
 class of product, regardless of the status of the particular user.

 To be a consumer product, a product must have "minimal functionality" for
 purposes other than display of "Relevant Legal Notices".
 For example, a "smart" toothbrush that only displays legal notices is not
 a consumer product.

 The "Installation Information" for a User Product means any methods,
 procedures, authorization keys, or other information required to install
 and execute modified versions of a covered work in that User Product from
 a modified version of its Corresponding Source. The information must suffice
 to ensure that the continued functioning of the modified object code is in
 no case prevented or interfered with because modifications have been made.

 If you convey an object code work under this section in, or with, or
 specifically for use in a User Product, and the conveying occurs as part
 of a transaction in which the right of possession and use of the User Product
 is transferred to the recipient in perpetuity or for a fixed term (regardless
 of how long the term is), the Corresponding Source conveyed under this section
 must be accompanied by the Installation Information. But this requirement does
 not apply if neither you nor any third party retains the ability to install
 modified object code on the User Product (for example, the work has been
 installed in ROM).

 The requirement to provide Installation Information does not include a
 requirement to continue to provide network services, or any services
 necessary for a User Product to function, if the network services cease
 to be provided for other reasons.

 7. Additional Terms.

 "Additional permissions" are terms that supplement the terms of this License
 by making exceptions from one or more of its conditions. Additional
 permissions that are applicable to the entire Program shall be treated as
 if they were included in this License, to the extent that they are valid under
 applicable law. If additional permissions apply only to part of the Program,
 that part may be used separately under those permissions, provided the
 rest of the Program continues to be governed by this License.

 When you convey a covered work, you may elect to remove any additional
 permissions from that covered work, or from any part of it. (Additional
 permissions may be written to require their own removal in certain cases
 when you modify the work.) You may place additional permissions on material,
 added by you to a covered work, for which you have or can assert appropriate
 copyright permission.

 Notwithstanding any other provision of this License, for material you add to
 a covered work, you may (if authorized by the copyright holders of that
 material) supplement the terms of this License with terms:

 a) Disclaiming warranty or limiting liability differently from the terms of
    sections 15 and 16 of this License; or
 b) Requiring preservation of specified ample legal notices or author
    attributions in that material or in the Appropriate Legal Notices
    displayed by works containing it; or
 c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in reasonable
    ways as differing from the original version; or
 d) Limiting the use for publicity purposes of names of licensors or authors
    of the material; or
 e) Declining to grant rights under trademark law for use of some trade names,
    trademarks, or service marks; or
 f) Requiring indemnification of licensors and authors of that material by
    anyone who conveys the material (or modified versions of it) with
    contractual assumptions of liability to the recipient, for any liability
    that these contractual assumptions directly impose on those licensors and
    authors.

 All other non-permissive additional terms are considered "further
 restrictions" within the meaning of section 10. If the Program as you received
 it, or any covered work you convey, contains such further restrictions, you
 must remove those restrictions before conveying it. You may not impose any
 further restrictions on any covered work so conveyed. If you try to impose
 further restrictions, or if you apply further terms that are "further
 restrictions", you understand and agree that this License will be
 immediately terminated as to you for any such work. However, if you are
 able to cure such a violation, then the License will be reinstated
 automatically, provided you comply with all terms of this License.

 8. Termination.

 You may not propagate or modify a covered work except as expressly provided
 under this License. Any attempt otherwise to propagate or modify it is void,
 and will automatically terminate your rights under this License (including
 any patent licenses granted under the third paragraph of section 11).

 However, if you cease all violation of this License, then your license from a
 particular copyright holder is reinstated (a) provisionally, unless and
 until the copyright holder explicitly and finally terminates your license,
 and (b) permanently, if the copyright holder fails to notify you of the
 violation by any reasonable means prior to 60 days after you cease the violation.

 Moreover, your license from a particular copyright holder is reinstated
 permanently if the copyright holder notifies you of the violation by some
 reasonable means, this is the first time you have received notice of
 violation of this License (for any work) from that copyright holder, and you
 cure the violation prior to 30 days after your receipt of the notice.

 Termination of your rights under this section does not terminate the patent
 licenses of parties who have received copies or rights from you under this
 License. If you cannot convey a covered work so as to satisfy simultaneously
 your obligations under this License and any other pertinent obligations, then
 as a consequence you may not convey it at all. For example, if you agree to
 terms that obligate you to collect a royalty for conveying the Program, and
 the only way you could satisfy that obligation is to forego the privileges
 permitted by this License, then you must not convey the Program.

 9. Acceptance Not Required for Having Copies.

 You are not required to accept this License in order to receive or run a copy
 of the Program. Ancillary propagation of a covered work occurring solely as a
 consequence of using peer-to-peer transmission to receive a copy likewise does
 not require acceptance. However, nothing other than this License grants you
 permission to propagate or modify any covered work. These actions infringe
 copyright if you do not accept this License. Therefore, by modifying or
 propagating a covered work, you indicate your acceptance of this License to do
 so.

 10. Automatic Licensing of Downstream Recipients.

 Each time you convey a covered work, the recipient automatically receives a
 license from the original licensors, to run, modify and propagate that work,
 subject to this License. You are not responsible for enforcing compliance by
 third parties with this License.

 An "entity transaction" is a transaction transferring control of an
 organization, or substantially all assets of one, or subdividing an
 organization, or merging organizations. If propagation of a covered work
 occurs as a consequence of an entity transaction, you acknowledge that you
 cannot impose any further restrictions on the propagation of any covered
 works.

 11. Patents.

 A "contributor" is a copyright holder who authorizes use under this License
 of the Program or a work on which the Program is based. The work thus
 licensed is called the "contributor version".

 A contributor's "essential patent claims" are all patent claims owned or
 controlled by the contributor, whether already acquired or hereafter acquired,
 that would be infringed by making, using, or selling the contributor version,
 but do not include claims that would be infringed only as a consequence of
 further modification of the contributor version. For purposes of this
 definition, "control" includes the right to grant patent sublicenses in a
 manner consistent with the requirements of this License.

 Each contributor grants you a non-exclusive, worldwide, royalty-free patent
 license under the contributor's essential patent claims, to make, use, sell,
 offer for sale, import and otherwise run, modify and propagate the contents
 of its contributor version.

 In the following three paragraphs, a "patent license" is any express
 agreement or commitment, however denominated, not to enforce a patent (such
 as an express permission to practice a patent or covenant not to sue for
 patent infringement). To "grant" such a patent license to a party means to
 make such an agreement or commitment not to enforce a patent against the
 party.

 If you convey a covered work, you waive any patent license that would
 otherwise be necessary from your contribution to that covered work, and
 promise not to assert any patent claims against any party for infringement
 of patents that you own or control, to the extent that such infringement
 is solely caused by making, using, or selling the covered work, or offering
 it for sale or import.

 You also agree that, if you convey a covered work, you will not knowingly
 arrange or permit the imposition of any further restrictions on the recipients'
 exercise of the rights granted herein. This means, for example, that you may
 not enter into a patent license agreement that would effectively prohibit
 recipients from making, using, or selling the Program.

 12. No Surrender of Others' Freedom.

 If conditions are imposed on you (whether by court order, agreement or otherwise)
 that contradict the conditions of this License, they do not excuse you from
 the conditions of this License. If you cannot convey a covered work so as to
 satisfy simultaneously your obligations under this License and any other
 pertinent obligations, then as a consequence you may not convey it at all.
 For example, if you agree to terms that obligate you to collect a royalty for
 conveying the Program, and the only way you could satisfy that obligation is to
 forego the privileges permitted by this License, then you must not convey the
 Program.

 13. Use with the GNU Affero General Public License.

 Notwithstanding any other provision of this License, you have permission to
 link or combine any covered work with a work licensed under version 3 of the
 GNU Affero General Public License into a single combined work, and to convey
 the resulting work. The terms of this License will continue to apply to the
 part which is the covered work, but the special requirements of the GNU Affero
 General Public License, section 13, concerning interaction through a network
 will apply to the combination as such.

 14. Revised Versions of this License.

 The Free Software Foundation may publish revised and/or new versions of the
 GNU General Public License from time to time. Such new versions will be
 similar in spirit to the present version, but may differ in detail to address
 new problems or concerns.

 Each version is given a distinguishing version number. If the Program specifies
 that a certain numbered version of the GNU General Public License "or any later
 version" applies to it, you have the option of following the terms and conditions
 either of that specified version or of any later version published by the
 Free Software Foundation. If the Program does not specify a version number of
 the GNU General Public License, you may choose any version ever published by the
 Free Software Foundation.

 If the Program specifies that a proxy can decide which future versions of the
 GNU General Public License can be used, that proxy's public statement of
 acceptance of a version permanently authorizes you to choose that version for
 the Program.

 Later license versions may give you additional or different permissions. However,
 no additional obligations are imposed on any author or copyright holder as a
 result of choosing a later version.

 15. Disclaimer of Warranty.

 THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
 EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER
 PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER
 EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO
 THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM
 PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
 CORRECTION.

 16. Limitation of Liability.

 IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL
 ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE
 PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL,
 SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY
 TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING
 RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE
 OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR
 OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

 17. Interpretation of Sections 15 and 16.

 If the disclaimer of warranty and limitation of liability provided above
 cannot be given local legal effect according to their terms,
 reviewing courts shall apply the strongest disclaimer of all implied warranties
 and limitation of liability possible that are permitted by the local law.

            END OF TERMS AND CONDITIONS

    How to Apply These Terms to Your New Programs

 If you develop a new program, and you want it to be of the greatest possible
 use to the public, the best way to achieve this is to make it free software
 which everyone can redistribute and change under these terms.

 To do so, attach the following notices to the program. It is safest to
 attach them to the start of each source file to most effectively state the
 exclusion of warranty; and each file should have at least the "copyright"
 line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

 Also add information on how to contact you by electronic and paper mail.

 If the program does not do interactive_mode, make a "non-interactive_mode"
 interface instead.

 The GNU General Public License does not permit incorporating your program into
 proprietary programs. If your program is a subroutine library, you may consider
 it more useful to permit linking proprietary applications with the library. If
 this is what you want to do, use the GNU Lesser General Public License instead of
 this License.
"""


text_area.insert(tk.END, license_text)
text_area.config(state=tk.DISABLED)

root.mainloop()