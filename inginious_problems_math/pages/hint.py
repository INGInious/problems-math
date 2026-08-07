# -*- coding: utf-8 -*-
#
# This file is part of INGInious. See the LICENSE and the COPYRIGHTS files for
# more information about the licensing of this file.

from flask import request, session
from werkzeug.exceptions import Forbidden

from inginious.frontend.courses import Course
from inginious.frontend.pages.utils import INGIniousAuthPage
from inginious.frontend.pages.course import handle_course_unavailable
from inginious.frontend.parsable_text import ParsableText


class HintPage(INGIniousAuthPage):
    def is_lti_page(self):
        return session.is_lti

    def POST_AUTH(self):
        data = request.form
        username = session.username
        language = session.language
        courseid = data.get("courseid", None)
        taskid = data.get("taskid", None)

        course = Course.get(courseid)
        if not self.user_manager.course_is_open_to_user(course, username, self.is_lti_page()):
            return handle_course_unavailable(self.user_manager, course)

        task = course.get_task(taskid)
        if not self.user_manager.task_can_user_submit(course, task, username, None, self.is_lti_page()):
            raise Forbidden(_("Task unavailable"))

        problemid = data.get("problemid", "")
        problems = task.get_problems()
        hints = ""
        for problem in problems:
            if problem.get_id() == problemid:
                hints = str(ParsableText(problem.gettext(language, problem._hints)))

        #TODO: Uncomment me when state and hints are fully implemented
        #if hints:
        #    user_tasks = self.database.user_tasks.find_one({"username": username, "courseid": courseid,
        #                                                    "taskid": taskid})
        #    try:
        #        state = json.loads(user_tasks.get("state", "{}"))
        #    except:
        #        state = {}
        #
        #    state.setdefault("hints", {})[problemid] = True
        #    self.database.user_tasks.update_one({"username": username, "courseid": courseid,
        #                                         "taskid": taskid}, {"$set": {"state": json.dumps(state)}})

        return hints
