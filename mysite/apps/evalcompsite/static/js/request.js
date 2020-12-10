import { validationMixin } from 'vuelidate'
import {required, minLength, maxLength, email} from 'vuelidate/lib/validators'

new Vue({
	el: '#request-app'
	mixins: [validationMixin],
	data() {
		return {
			form: {
				last_name: '',
				first_name: '',
				patronymic: '',
				email: '',
				phone_number: '+7',
				eval_object: '',
				aim: '',
				address: '',
				price: '',
				comment: '',
			},
			eval_objects: [
				{
					label: 'Выберите один из вариантов',
					value: ''
				},
				{
					label: 'Квартира',
					value: 'Квартира'
				},
				{
					label: 'Дом с земельным участком',
					value: 'Дом с земельным участком'
				},
				{
					label: 'Вступление в наследство',
					value: 'Вступление в наследство'
				},
				{
					label: 'Земельный участок',
					value: 'Земельный участок'
				},
				{
					label: 'Акции',
					value: 'Акции'
				},
				{
					label: 'Коммерческая недвижимость',
					value: 'Коммерческая недвижимость'
				},
				{
					label: 'Оспаривание кадастровой стоимости',
					value: 'Оспаривание кадастровой стоимости'
				},
				{
					label: 'Другое',
					value: 'Другое'
				}
			],
			aims: [
				{
					label: 'Выберите один из вариантов',
					value: ''
				},
				{
					label: 'Кредитование',
					value: 'Кредитование'
				},
											{
					label: 'Страхование',
					value: 'Страхование'
				},
				{
					label: 'Вступление в наследство',
					value: 'Вступление в наследство'
				},
				{
					label: 'Кредитование',
					value: 'Кредитование'
				},
				{
					label: 'Для сдачи в аренду',
					value: 'Для сдачи в аренду'
				},
				{
					label: 'Для решения имущественных споров',
					value: 'Для решения имущественных споров'
				},
				{
					label: 'Другое',
					value: 'Другое'
				}
			]
		}
	},
	validations: {
		form: {
				last_name: {required},
				first_name: {required},
				email: {required, email},
				phone_number: {required, minLength: minLength(12), maxLength: maxLength(12)},
				eval_object: {required},
				aim: {required},
				address: {required}
			},
	},
	methods: {
		checkForm() {
			this.$v.form.$touch()
			if (this.$v.form.$error) {
				console.log('Валидация прошла успешно')
			}
		}
	}
}

)