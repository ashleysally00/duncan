# src/confidence_quiz.py

class ConfidenceQuiz:
    def __init__(self):
        self.questions = [
            {
                "id": 1,
                "question": "When you have a unique idea during a team meeting and notice others are hesitant to speak up, do you decide to present your idea confidently?",
                "options": {
                    "A": "I am confident in my thoughts and present my idea clearly, providing data or examples to back it up and engage others in a meaningful discussion.",
                    "B": "I share my idea, but I feel a bit uncertain about how it will be received, so I might not put my full energy into presenting it.",
                    "C": "I decide to hold back and keep my idea to myself to avoid drawing attention or possibly disrupting the meeting's flow."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 2,
                "question": "How do you typically respond when a colleague interrupts you during a meeting or conversation?",
                "options": {
                    "A": "I calmly make eye contact, wait for a pause, and then politely but firmly ask if I can finish my thought before we move on, ensuring my voice is heard.",
                    "B": "I usually let them continue to avoid any discomfort, though it does bother me. I feel torn between staying polite and standing up for my own voice.",
                    "C": "I quickly apologize or let my point drop, rushing to finish or not saying anything further. I worry about being seen as too assertive."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 3,
                "question": "When a colleague receives a promotion you were expecting, do you schedule a meeting to discuss your career path and future opportunities?",
                "options": {
                    "A": "I make it a point to set up a meeting with my manager to understand what areas I can improve and to explore potential growth opportunities.",
                    "B": "I think about scheduling a meeting to discuss my career path but might hesitate or delay it due to uncertainty.",
                    "C": "I decide not to bring it up and avoid the conversation entirely, preferring not to draw attention to myself or feel uncomfortable."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 4,
                "question": "When you receive feedback that your recent project could be improved, how do you handle it?",
                "options": {
                    "A": "I actively seek out resources, training, or advice from peers to understand where I can improve and make sure I’m growing from the feedback.",
                    "B": "I acknowledge the feedback and consider it, but I don’t take significant steps to improve immediately. I might feel hesitant about reaching out.",
                    "C": "I feel discouraged by the feedback and decide not to pursue further learning or adjustments, fearing it might highlight my weaknesses."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 5,
                "question": "During a performance review, do you request a salary increase?",
                "options": {
                    "A": "I confidently discuss my contributions, highlight my accomplishments, and negotiate a fair raise based on my impact in the company.",
                    "B": "I feel hesitant but prepare a list of my achievements. I bring it up, though I may not push strongly if it’s not well-received.",
                    "C": "I avoid bringing up a raise altogether, worried that I might come across as demanding or get rejected."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 6,
                "question": "If a client or co-worker suggests changes that you believe could negatively impact the project’s success, how do you respond?",
                "options": {
                    "A": "I express my concerns clearly, explaining potential issues and proposing alternative solutions to keep the project on track.",
                    "B": "I mention my concerns but am hesitant to fully oppose their suggestion or offer a different approach.",
                    "C": "I agree with the changes to avoid any conflict or friction, even if I worry it might harm the project."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 7,
                "question": "What do you do when you notice a recurring issue in your workflow?",
                "options": {
                    "A": "I take initiative to suggest a solution or new process to address the issue, and I offer to help with its implementation.",
                    "B": "I mention the issue casually but wait for someone else to propose a solution or take action.",
                    "C": "I don’t bring it up, hoping that it will eventually resolve itself or that someone else will address it."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 8,
                "question": "Facing a tight deadline, are you able to delegate tasks?",
                "options": {
                    "A": "I confidently assign tasks to team members, communicate expectations clearly, and make sure everyone is aligned.",
                    "B": "I delegate tasks, but I feel uneasy about communicating my needs and worry if I’m being too demanding.",
                    "C": "I end up taking everything on myself, feeling stressed but preferring not to rely on others."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 9,
                "question": "You attend a networking event where you don't know many people. What do you do?",
                "options": {
                    "A": "I introduce myself confidently to others, start conversations, and exchange contact information to build connections.",
                    "B": "I feel a bit nervous but manage to talk to a few people, sticking to lighter topics and small talk.",
                    "C": "I avoid initiating conversations and mostly keep to myself, feeling overwhelmed and unsure of how to engage."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 10,
                "question": "During salary negotiations, what's your typical approach?",
                "options": {
                    "A": "Accept the initial offer to avoid seeming demanding",
                    "B": "Research market rates and negotiate based on your value",
                    "C": "Feel uncomfortable but ask for a small increase"
                },
                "scores": {
                    "A": 1,
                    "B": 3,
                    "C": 2
                }
            },
            {
                "id": 11,
                "question": "When a colleague takes credit for your work, do you address the situation by discussing it directly with them and seeking recognition?",
                "options": {
                    "A": "I have a respectful conversation to clear up any confusion and ensure that my contribution is acknowledged.",
                    "B": "I hint at the situation indirectly but avoid bringing it up explicitly to prevent confrontation.",
                    "C": "I choose not to address it, preferring to avoid any potential conflict or tension."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 12,
                "question": "What do you do when you’re asked to mentor a junior employee?",
                "options": {
                    "A": "I gladly take on the mentoring role, providing guidance and support to help them succeed.",
                    "B": "I agree to mentor them but sometimes feel unsure about the best advice to give.",
                    "C": "I feel uncomfortable mentoring, questioning my own ability to guide others effectively."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 13,
                "question": "If a project doesn’t go as planned, how do you share feedback?",
                "options": {
                    "A": "I review what went wrong and provide constructive feedback to help the team improve.",
                    "B": "I consider sharing feedback but find it hard to speak up about areas of improvement.",
                    "C": "I avoid discussing the project’s issues to keep the peace and prevent discomfort."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 14,
                "question": "In a team meeting, you strongly disagree with a colleague's approach. What do you typically do?",
                "options": {
                    "A": "Wait until after the meeting to discuss it privately with your colleague",
                    "B": "Raise your concerns during the meeting, presenting your alternative with supporting data",
                    "C": "Keep your opinion to yourself to avoid potential conflict"
                },
                "scores": {
                    "A": 2,
                    "B": 3,
                    "C": 1
                }
            },
            {
                "id": 15,
                "question": "If a team member disagrees with your approach to a project, do you engage in a constructive discussion to find a common solution?",
                "options": {
                    "A": "I listen to their perspective and work toward a compromise that benefits the project.",
                    "B": "I discuss it but feel somewhat uncomfortable resolving disagreements.",
                    "C": "I avoid the discussion, letting the disagreement persist to prevent friction."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 16,
                "question": "You've achieved a significant milestone in your project. How do you handle it?",
                "options": {
                    "A": "Briefly mention it in your status report",
                    "B": "Share the achievement and credit your team's contributions",
                    "C": "Wait for others to notice and mention it"
                },
                "scores": {
                    "A": 2,
                    "B": 3,
                    "C": 1
                }
            },
            {
                "id": 17,
                "question": "When facing a challenging task outside your comfort zone, you usually:",
                "options": {
                    "A": "Take it on as a growth opportunity, seeking help when needed",
                    "B": "Feel anxious but try your best to complete it",
                    "C": "Try to pass it to someone more experienced"
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 18,
                "question": "If you notice a colleague struggling with their workload, what do you do?",
                "options": {
                    "A": "I offer my assistance and check in to see how I can help ease their workload.",
                    "B": "I offer help, though I feel unsure about the best way to assist them.",
                    "C": "I choose not to get involved, focusing on my own responsibilities."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 19,
                "question": "Your manager asks if anyone wants to lead an important new project. What's your response?",
                "options": {
                    "A": "Immediately volunteer, highlighting your relevant skills",
                    "B": "Wait to see if anyone else volunteers first",
                    "C": "Consider volunteering but worry about potential failure"
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            },
            {
                "id": 20,
                "question": "When networking with other professionals, how are your conversations?",
                "options": {
                    "A": "I engage thoughtfully, ask insightful questions, and build valuable connections.",
                    "B": "I make small talk but feel nervous about delving deeper into conversations.",
                    "C": "I keep conversations short and light, avoiding more meaningful interactions."
                },
                "scores": {
                    "A": 3,
                    "B": 2,
                    "C": 1
                }
            }
        ]
        
    def calculate_score(self, answers):
        """Calculate total score and return feedback."""
        total_score = sum(self.questions[i]["scores"][answer] for i, answer in enumerate(answers))
        max_possible = len(self.questions) * 3
        score_percentage = (total_score / max_possible) * 100
        
        if score_percentage >= 80:
            confidence_level = "High Confidence"
            feedback = self._get_high_confidence_feedback()
        elif score_percentage >= 60:
            confidence_level = "Moderate Confidence"
            feedback = self._get_moderate_confidence_feedback()
        else:
            confidence_level = "Developing Confidence"
            feedback = self._get_developing_confidence_feedback()
        
        return {
            "score": total_score,
            "max_score": max_possible,
            "percentage": score_percentage,
            "feedback": feedback
        }
    
    def _get_high_confidence_feedback(self):
        return {
            "level": "High Confidence",
            "summary": "You exhibit strong workplace confidence!",
            "strengths": [
                "Comfortable taking initiative",
                "Effective at self-advocacy",
                "Strong leadership potential"
            ],
            "next_steps": [
                "Consider mentoring others to build their confidence",
                "Take on stretch assignments to further grow",
                "Share your experiences in professional forums"
            ],
            "interview_tips": [
                "Use specific examples of leadership in interviews",
                "Highlight instances where your confidence led to success",
                "Express interest in growth opportunities"
            ]
        }
    
    def _get_moderate_confidence_feedback(self):
        return {
            "level": "Moderate Confidence",
            "summary": "You have a good foundation of confidence with room to grow.",
            "strengths": [
                "Capable of speaking up when necessary",
                "Willing to take on challenges",
                "Shows potential for leadership"
            ],
            "next_steps": [
                "Practice voicing your opinions more in meetings",
                "Take on more visible projects",
                "Set specific goals for professional growth"
            ],
            "interview_tips": [
                "Prepare examples of overcoming challenges",
                "Practice discussing achievements comfortably",
                "Focus on growth mindset in responses"
            ]
        }
    
    def _get_developing_confidence_feedback(self):
        return {
            "level": "Developing Confidence",
            "summary": "You have opportunities to build your workplace confidence.",
            "strengths": [
                "Thoughtful in approach to work",
                "Careful consideration of options",
                "Potential for growth"
            ],
            "next_steps": [
                "Start with small wins to build confidence",
                "Find a mentor for guidance and support",
                "Practice self-advocacy in low-stakes situations"
            ],
            "interview_tips": [
                "Focus on learning experiences and growth",
                "Prepare thoroughly to boost confidence",
                "Practice interview responses with trusted friends"
            ]
        }
