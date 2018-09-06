from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import CommentForm
from comment.models import Comment
from django.shortcuts import redirect

class CommentShowMixin(object):
    def get_comments(self):
        target = self.request.path
        comments = Comment.objects.filter(target=target)
        return comments

    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm(),
            'comment_list': self.get_comments(),
        })
        return super(CommentShowMixin, self).get_context_data(**kwargs)
    

class CommentView(TemplateView):
    template_name = 'template/comment/result.html'

    def post(self, request, *args, **kwargs):
        # TODO: 获取path
        comment_form = CommentForm(request.POST)
        target = request.POST.get('target')
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target
        }
        return self.render_to_response(context)



    


